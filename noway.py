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
#퀴즈) 우리 학교에서 파이썬 코딩대회 주최
참석률 높이려 댓글 이벤트 진행
댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰
추첨프로그램 작성하여라



'''
