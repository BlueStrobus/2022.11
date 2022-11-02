'''# 자료구조의 변경 -> 이름= 구조(이름)

bee = {"말벌", "장수말벌", "꿀벌"}  # {중괄호} set
print(bee, type(bee))  # <class 'set'>

bee = list(bee)  # [대괄호] list
print(bee, type(bee))  # <class 'list'>

bee = tuple(bee)  # (소괄호) tuple
print(bee, type(bee))  # <class 'tuple'>

bee = set(bee)
print(bee, type(bee))  # <class 'set'>

# 출력
# {'장수말벌', '말벌', '꿀벌'} <class 'set'>
# ['장수말벌', '말벌', '꿀벌'] <class 'list'>
# ('장수말벌', '말벌', '꿀벌') <class 'tuple'>
# {'장수말벌', '말벌', '꿀벌'} <class 'set'>

#######################

#######################
'''  # 퀴즈) 우리 학교에서 파이썬 코딩대회 주최
참석률 높이려 댓글 이벤트 진행
댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰
추첨프로그램 작성하여라

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라 가정
조건2: 댓글 내용과 무관하게 무작위 추천, 중복 불가
조건3: random모듈의 shuffle과 sample사용

(출력예제)
--당첨자 발표--
치킨 당첨자: 1
커피 당첨자: [2, 3, 4]
--축하합니다--

'''
####
from random import *
user = range(1, 21)
user = list(user)
print(user)

winers = sample(user, 4)

print(
    "--당첨자 발표--\n치킨 달첨자: {}\n커피 당첨자: {}\n--축하합니다--".format(winers[0], winers[1:4]))

'''
'''
# if

watter = "비"
if watter == "비":
    print("우산을 챙기세요")
'''

# for 반복문
# for wether in
