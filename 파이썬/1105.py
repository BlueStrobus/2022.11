#지역변수와 전역변수

#지역변수 : 함수내에서만 쓸 수 있는 것
#전역변수 : 프로그램 내에서 언제든지 쓸 수 있는 것

'''
gun=10

def checkpoint(soldiers): #경계 근무
    gun = gun - soldiers #gun은 지역변수라 위에꺼랑 연관없음. 오류뜬다.
    print("[함수 내] 남은 총 : {0}".format(gun))

#print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
'''

gun=10 #전역변수 넣어주면 외부의 변수에도 변화가 생김
def checkpoint(soldiers): #경계 근무
    global gun #변수앞에 global 띄루기 해서 전역변수를 넣어줌
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))