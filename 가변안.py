# #가변인자 *변수이름
'''def profile(name,age, lang1,lang2,lang3,lang4,lang5): #함수의 키는 ""사용x
    print("이름: {0}\t나이 : {1}\t".format(name,age),end=" ")
    print(lang1,lang2,lang3,lang4,lang5)

profile("알프레드",45,"c","c++","C#","자바","F#")
# #알프레드 45 c c++ C# 자바 F#'''


def profile(name,age,*lang): #함수의 키는 ""사용x
    print("이름: {0}\t나이 : {1}\t".format(name,age),end=" ")
    for languige in lang:
        print(languige,end=" ")
    print()

profile("알프레드",45,"c","c++","C#","자바","F#")
profile("haby dent", 34, "python")
profile("그레이슨",23,"c","c++","자바","python","go","rust")
'''
이름: 알프레드  나이 : 45        c c++ C# 자바 F# 
이름: haby dent 나이 : 34        python
이름: 그레이슨  나이 : 23        c c++ 자바 python go rust'''