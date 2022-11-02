import tkinter  # Gui모듈 포함시키기
# import try_tkinter_only_bagground
# '''#윈도우창만들기-기본################
# # newwin = tkinter.Tk()  # 윈도우창 생성
# # newwin.mainloop()  # 위도우가 종료될 때까지 실행
# # ###########기본적인 tkinter 윈도우창만 만들기'''

# # 이름, 창 크기 지정
# windy = tkinter.Tk()
# windy.title("비엽성알러지 싫어")  # 윈도우창 이름
# windy.geometry("640x400+100+100")  # 윈도우창 크기
# # 윈도우이름.geometry("너비x높이+x좌표+y좌표")
# windy.resizable(1, 1)  # 아니면 False,False
# # 윈도우이름.resizeable(상하, 좌우)을 이용하여 윈도우 창의 창 크기 조절 가능 여부를 설정할 수 있습니다. True로 설정할 경우 윈도우 창의 크기를 조절할 수 있습니다.
# # Tip : resizeable()을 적용할 때, True=1, False=0(크기조절안됨)을 의미하여 상수를 입력해도 적용이 가능합니다.
# ###########################

# 내용 entry 만들기
lalalabel = tkinter.Label(windy, text="클라이밍수업가라.")
lalalabel.pack()
# 위젯이름=tkinter.Label(윈도우창, text="내용")을 사용하여 윈도우 창에 Label 위젯을 설정할 수 있습니다.
# 위젯이름.pack()을 사용하여 위젯을 배치할 수 있습니다.

#####
# while True:
#     lalalabel = tkinter.Label(windy, text=input("말해봐"))
#     lalalabel.pack()
# # input한 글이 아랫줄에 적힘 ...반복 #창 끄고나서 입력하면 오류 발생
#########

# 라벨(변하지 않는 텍스트)
label = tkinter.Label(windy, text="홀드", width=30,
                      height=5, fg="blue", relief="solid")
label.pack()

windy.mainloop()
