#컨티뉴, 브레이크

# 컨티뉴: 없는거 빼고 계속 진행
nobook = [7]
absent = [2, 5]  # 결석
for student in range(1, 11):  # 1~20
    if student in absent:
        continue  # 윗줄에 조건같은거:   아랫줄에 continue 적기
    elif student in nobook:
        print("오늘수업 여기까지. {0}은 교무실로 와라".format(student))
# 브레이크
        break  # 종료, 끝냄
    print("{0}, 책을 읽어라".format(student))
