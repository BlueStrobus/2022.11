# 랜덤 쓰는 방법 외우라고!!!!!
from random import randint

count = int(0)
for night in range(1, 50):
    #print(night, type(night))
    # #요소가 가로로 나오기를 바랬는데...
    wait = randint(5, 51)

    if 5 <= wait <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(night, wait))
        count += 1

    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(night, wait))

print(count)
