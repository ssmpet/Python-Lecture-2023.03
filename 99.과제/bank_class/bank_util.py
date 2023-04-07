
# 계좌는 계좌번호, 소유주, 잔액으로 구성됨
# 계좌번호는 생성된 시점의 시간, 분, 초 6자리로 구성됨.
# 이름과 금액을 입력으로 받아서 account에 새로운 항목을 추가

import pickle
import datetime as dt 
from account import Account

def is_name(name, account):
    for acc in account:
        if acc.owner == name:
            return True
    return False


def is_ano(ano, account):
    for acc in account:
        if acc.ano == ano:
            return True
    return False

def list_account(account):
    for acc in account:
        print(acc)

def create_account(account):

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
    new_account = Account(ano, name, price)
    account.append(new_account)
    print(new_account)
    
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

            if not is_ano(ano, account) :
                print(f'\n계좌가 없습니다. 계좌를 먼저 개설해 주세요.')
                return
            break

    # 금액을 받는 부분
    price = 0
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

  
    for acc in account:
        if acc.ano == ano:
            acc.deposit(price)
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

            if not is_ano(ano, account) :
                print(f'\n계좌가 없습니다. 계좌를 먼저 개설해 주세요.')
                return
            break

    # 금액을 받는 부분
    while True:
        try : 
            price = int(input('\n찾을 금액을 입력하세요. > '))
        except:
            print('금액을 잘못 입력했습니다.')
            continue
        break

    for acc in account:
        if acc.ano == ano:
            acc.withdrow(price)
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
        account.append(Account('142603', '홍길동', 10000))

    return account