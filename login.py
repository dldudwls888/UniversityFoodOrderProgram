# tkinter를 사용하기 위한 import
from tkinter import *
from tkinter import ttk
from datetime import datetime
import tkinter as tk
import webbrowser

# tkinter 객체 생성
window = Tk()
window.title("도시락 예약 프로그램")
window.option_add("*Font", "맑은고딕 19 bold")
window.geometry("400x500")

# 배경과 학교로고
back = PhotoImage(file = "background.png")
logo = PhotoImage(file = "suwonuniversity.png")

# id리스트와 입력받을아이디, 비밀번호 변수 선언
id_list = {"17018063", "18012035", "15018044"} #받은학번
id, password = StringVar(), StringVar() #입력받을학번,비밀번호
failcount = 0

# id리스트와 입력받은 아이디 비교
def check_data():
    global failcount
    idgive = id.get()
    # 로그인 성공 시 order2 실행 / txt파일 생성
    if idgive in id_list and password.get() == "suwon1234":
        print("[로그인성공] 도시락 멤버입니다!")
        txtfile = open("[점심] 기숙사생 도시락 예약 현황.txt", 'a')
        output = "[" + idgive + "] 학생의 [점심] 도시락 예약 현황\n예약시각 : " + str(datetime.now()) + "\n[22시 이후 예약 반영 X]\n■■■■■■■■■■■■■■\n"
        txtfile.write(output)
        txtfile.close()
        txtfile = open("[저녁] 기숙사생 도시락 예약 현황.txt", 'a')
        output = "[" + idgive + "] 학생의 [저녁] 도시락 예약 현황\n예약시각 : " + str(datetime.now()) + "\n[22시 이후 예약 반영 X]\n■■■■■■■■■■■■■■\n"
        txtfile.write(output)
        txtfile.close()
        import orderlunch
    else:
        failcount = failcount+1
        print("[로그인실패] 학번과 비밀번호를 확인해주세요")
        print('로그인 %d회 실패하였습니다' % failcount)
    
    if failcount >= 3:
        print("로그인 3회 이상 실패! 프로그램 종료합니다")
        quit()

# ID/PW 찾기 링크연결
def url_open():
    url = 'https://portal.suwon.ac.kr/enview/usw/inquityType.jsp?langKnd=ko'
    webbrowser.open(url)

# id, pw, login UI 부분
ttk.Label(window, text = "background", image = back).place(x=0, y=0)
ttk.Label(window, text = "logo", image = logo).grid(row = 1, column = 0, padx = 0, pady = 0)
tk.Label(window, text = "■ 학번 ", relief=SOLID, borderwidth=3).grid(row = 3, column = 0, padx = 10, pady = 10, sticky=W)
tk.Label(window, text = "■ 암호 ", relief=SOLID, borderwidth=3).grid(row = 4, column = 0, padx =10, pady = 10, sticky=W)
ttk.Entry(window, textvariable = id).grid(row = 3, column = 0, padx = 0, pady = 0, sticky=E)
ttk.Entry(window, textvariable = password).grid(row = 4, column = 0, padx = 0, pady = 0, sticky = E)
tk.Button(window, text = "Login", command = check_data, font=("맑은 고딕", 12, "bold"), width= 26).grid(row = 5, column = 0, padx = 5, pady = 5, sticky=E)
tk.Button(window, text = "ID/PW 찾기", command= url_open, font=("맑은 고딕", 12, "bold"), width= 10).grid(row = 5, column = 0, padx = 5, pady = 5, sticky=W)
ttk.Label(window, text = datetime.now()).grid(row=6, column=0, padx=0, pady = 30, sticky = S)

window.mainloop()