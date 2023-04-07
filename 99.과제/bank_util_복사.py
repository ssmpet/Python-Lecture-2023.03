
# 계좌는 계좌번호, 소유주, 잔액으로 구성됨
# 계좌번호는 생성된 시점의 시간, 분, 초 6자리로 구성됨.
# 이름과 금액을 입력으로 받아서 account에 새로운 항목을 추가

import datetime as dt 
import pickle


def is_name(name, account):
    for acc in account:
        if acc['소유주'] == name:
            return True
    return False


def get_ano_balance(ano, account):
    for acc in account:
        if acc['계좌번호'] == ano:
            return True, acc['잔액']

    return False, 0

def create_acount(account):
    while True:
        name = input('\n이름을 입력해주세요.[이전단계 : Q/q] > ')
        if name == '':
            continue
        else:
            if name == 'Q' or name == 'q':
                return

            if is_name(name, account) :
                print(f'\n{name}님은 이미 계좌가 생생되어 있는 분입니다.')
                print('다름 이름으로 만들어 주세요.')
                continue
            break

    # 금액을 받는 부분
    while True:
        try : 
            price = int(input('\n입금할 금액을 입력하세요. 최소 1,000원 이상입니다. > '))
        except:
            print('금액을 잘못 입력했습니다.')
            continue
        
        if price < 1000:
            print('최초 입력 금액은 1000원 이상입니다.')
            continue
        break

    # account 에 추가하기
    ano = dt.datetime.now().strftime('%H%M%S')
    account.append({'계좌번호':ano, '소유주':name, '잔액': price})
    print(f'{name}님의 계좌번호: {ano} 로 생성되었습니다.\n')

    # return account

# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 입금
# 입금
def deposit(account):
    while True:
        ano = input('\n계좌번호를 입력해주세요.[이전단계 : Q/q] > ')
        if ano == '':
            continue
        else:
            if ano == 'Q' or ano == 'q':
                return

            ano_check, money = get_ano_balance(ano, account)
            if not ano_check :
                print(f'\n계좌가 없습니다. 계좌를 먼저 개설해 주세요.')
                return
            break

    # 금액을 받는 부분
    while True:
        try : 
            price = int(input('\n입금할 금액을 입력하세요. 최소 1,000원 이상입니다. > '))
        except:
            print('금액을 잘못 입력했습니다.')
            continue
        
        if price < 1000:
            print('최소한 입력 금액은 1000원 이상입니다.')
            continue
        break

    money += price
    
    for acc in account:
        if acc['계좌번호'] == ano:
            acc['잔액'] = money
            break

# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 인출
def withdraw(account):
    while True:
        ano = input('\n계좌번호를 입력해주세요. (취소:Q/q) > ')
        if ano == '':
            continue
        else:
            if ano == 'Q' or ano == 'q':
                return

            ano_check, money = get_ano_balance(ano, account)
            if not ano_check :
                print(f'\n계좌가 없습니다. 계좌를 먼저 개설해 주세요.')
                return
            break

    # 금액을 받는 부분
    while True:
        try : 
            print(f'고객님의 잔액은 {money:,d} 원입니다.\n')
            price = int(input('\n찾을 금액을 입력하세요. > '))
        except:
            print('금액을 잘못 입력했습니다.')
            continue
        
        if money < price:
            print('찾을 금액이 잔액보다 큼니다.')
            continue
        break

    money -= price
    
    for acc in account:
        if acc['계좌번호'] == ano:
            acc['잔액'] = money
            break

def account_save(account):
    with open('data/bank.pkl', 'wb') as file:
        pickle.dump(account, file)
    
def account_read():
    account = []
    try: 
        with open('data/bank.pkl', 'rb') as file:
            account = pickle.load(file)
    except:
        pass

    return account