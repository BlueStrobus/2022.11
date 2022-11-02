from tkinter import *
entry = ""  # 이거 있는게 맞나?


def clisk(key):  # 함수 만들기 - def 쓰고 작명하고 (): 붙이고 indent 넣기
    if key == '=':  # 키가 '='버튼이면 수식을 계산하여 결과를 표시한다.
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, "오류!!!")
    elif key == 'C':
        entry.delete(0, END)
    else:
        entry.insert(END, key)


window = Tk()  # tk창 열기
window.title("간단한 계산기")

buttons = ['7', '8', '9', '+', 'C',
           '4', '5', '6', '-', '',
           '1', '2', '3', '*', '',
           '0', '.', '=', '/', '']

# 반복문으로 버튼 생성
i = 0
for b in buttons:
    def cmd(x=b): return clisk(X)  # lambda 람다:함수를 한줄로 만듦
    #lambda 매개변수 : 표현식
    but = Button(window, text=b, width=5, relief='ridge', command=cmd)
    # 뭐에 쓰는건지 찾기text=, width=,relief='뭔가',command=
    # text=  텍스트가 클릭한 x값(b)이다
    #width= 가로크기
    # relief='ridge'  relief : 프레임의 테두리 모양  ridge:산등성이
    # relief=' 다음에 flat, groove, raised, ridge, solid, sunken중하나 넣기
    but.grid(rou=i//5+1, column=i % 5)  # grid는 격자
    # // 두 값을 나눈 결과의 몫의 반환(정수 값)
    # # % 두 값을 나눈 결과의 나머지 반환
    i += 1

# 엔트리 위젯은 맨 욋줄의 5개의 셀에 걸쳐서 배치됨


'''
#  def의 이용 1. 긴 코드를 축약,2.마법의 모자 만들 깨 사용(f(x)같은거)
#  def 축약할이름() :
#     축약할긴코드들1
#     축약할긴코드들2
#2.마법모자
#def  모자(숫자) :  #숫자, 문자 다 가능
#   print(숫자 + 2)

# 모자(4)
# 모자(6)

# 3. 뭔가 내뱉기
# def 함수2() :
#     return 10

# print(함수2())
#  함수 안에는 return 이라는 키워드를 사용가능합니다.

# return은 "return 오른쪽에 있는 자료를 함수2 실행하고나서 퉤 뱉어라" 라는 뜻입니다. 
'''
