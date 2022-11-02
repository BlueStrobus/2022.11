# 한줄로 끝내는 for문
# 출석번호 1,2,3,4 -> 101,102,103,104
student = [1, 2, 3, 4]
print(student)

student = [i+100 for i in student]  # i에 student넣음
print(student)
