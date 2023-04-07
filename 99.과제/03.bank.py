import sys
import bank_util as bu


# 계좌는 계좌번호, 소유주, 잔액으로 구성됨
# 계좌번호는 생성된 시점의 시간, 분, 초 6자리로 구성됨.
# account = [
#     {'계좌번호':'142603','소유주':'홍길동', '잔액': 10000 }
# ]

account = []
account = bu.account_read()

while True:
    
    try: 
        menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5:종료 > '))
    except:
        print('잘못된 명령입니다.\n')
        continue

    if menu == 5:
        bu.account_save(account)
        sys.exit()

    if menu == 1:

        bu.create_acount(account)
        
    elif menu == 2:
        print()
        for acc in account:
            for key, val in acc.items():            
                print(f'{key}: {val}', end='\t')
            print()
        print()

    elif menu == 3:
        bu.deposit(account)
        print()
        
    elif menu == 4:
        bu.withdraw(account)
        print()
