def open_sesumi():  # 함수는 def로 시작해서 함수 이름 적고 :
    print("새로운 계좌 생성되었습니다")  # 그 아래 함수 적기
# 함수는 소환하기 전까지는 일 안함


def deposit(balanc, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balanc+money))
    return balanc+money  # 반환된 값은 balanc에 저장됨


def withdraw(balance, money):  # 출금
    if balanc >= money:  # 잔액보다 출금이 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balanc-money))
        return balanc-money

    else:  # 잔액이 출금보다 적음
        print("잔액이 모자랍니다. 잔액은 {}원입니다.".format(balanc))
        return balanc


balanc = 0  # 잔액
balanc = deposit(balanc, 1000)  # 1000원 입금
print(balanc)

balanc = withdraw(balanc, 200)
print(balanc)
