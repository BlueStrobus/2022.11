# #가변인자
# def profile(name,age, lang1,lang2,lang3,lang4,lang5): #함수의 키는 ""사용x
#     print("이름: {0}\t나이 : {1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# print("알프레드",45,"c","c++","C#","자바","F#")
# #알프레드 45 c c++ C# 자바 F#


def profile(name,age,*lang): #함수의 키는 ""사용x
    print("이름: {0}\t나이 : {1}\t".format(name,age),end=" ")
    print(*lang)

print("알프레드",45,"c","c++","C#","자바","F#")
print("haby dent", 34, "python")
print("그레이슨",23,"c","c++","자바","python","go","rust")
'''출력
알프레드 45 c c++ C# 자바 F#
haby dent 34 python
그레이슨 23 c c++ 자바 python go rust'''