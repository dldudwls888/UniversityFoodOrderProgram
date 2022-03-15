from os import write
from tkinter import *
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

# 도시락 종류와 주문 합계
price = {'제육볶음 도시락': 4500, '삼겹살 도시락': 5000, '닭갈비 도시락' : 4500, '스팸마요 컵밥': 3000}
order = []
sum1 = 0
counter=0

# 총 주문 금액 / textarea 생성
def add1(item1):
    global sum1
    this_price1 = price.get(item1)
    sum1 += this_price1
    order.append(item1)
    textarea1.insert(tk.INSERT,"[선택]" + item1 + " [가격] " + str(this_price1) + "원\n")
    label1['text'] = "주문 금액 : " + str(sum1) + "원"

# 주문 취소 버튼
def btn_cancel():
    msgbox = tk.messagebox.askquestion('주문 취소','도시락 주문을 취소하시겠습니까?')
    if msgbox == 'yes':
        txtfile = open("[점심] 기숙사생 도시락 예약 현황.txt", 'a')
        output = "■■■■■■■■■■■■■■\n▷▷▷▷▷▷▷▷주문 취소됨!!◁◁◁◁◁◁◁◁\n-------------------------------------------------\n"
        txtfile.write(output)
        txtfile = open("[저녁] 기숙사생 도시락 예약 현황.txt", 'a')
        output = "■■■■■■■■■■■■■■\n▷▷▷▷▷▷▷▷주문 취소됨!!◁◁◁◁◁◁◁◁\n-------------------------------------------------\n"
        txtfile.write(output)
        exit()

# 주문 확인 버튼
def btn_exit():
    global sum1
    msgbox = tk.messagebox.askquestion('주문 확인','도시락 주문을 마치시겠습니까?')
    if msgbox == 'yes':
        txtfile = open("[점심] 기숙사생 도시락 예약 현황.txt", 'a')
        output = "■■■■■■■■■■■■■■\n총 주문금액 : " + str(sum1) + "원\n-------------------------------------------------\n"
        txtfile.write(output)
        exit()

# 저녁 예약 버튼
def btn_dinner():
    global sum1
    msgbox = tk.messagebox.askquestion('저녁 예약','저녁 예약 화면으로 넘어가시겠습니까?')
    # 확인 시 order3 실행
    if msgbox == 'yes':
        txtfile = open("[점심] 기숙사생 도시락 예약 현황.txt", 'a')
        output = "■■■■■■■■■■■■■■\n총 주문금액 : " + str(sum1) + "원\n-------------------------------------------------\n"
        txtfile.write(output)
        import orderdinner

# txt파일 주문내역 추가
def increase_counter1(item1):
    txtfile = open("[점심] 기숙사생 도시락 예약 현황.txt", 'a')
    this_price = price.get(item1)
    output = str(item1) + " " + str(this_price) + "원\t■\n"
    txtfile.write(output)
    txtfile.close()


# 점심 도시락 주문 창 GUI
window = tk.Tk()
window.title("도시락 주문")
window.geometry("400x500")
back = PhotoImage(file = "background.png")
root = tk.Frame(window)
root.pack()
tk.Label(root, text="점심", fg="blue").grid(row=0, column=1)
tk.Button(root, text="제육볶음 도시락  [4500원]", bg = "black", fg = "white", font=("맑은 고딕", 11, "bold"), command=lambda: {add1('제육볶음 도시락'), increase_counter1('제육볶음 도시락')}, width=20).grid(row=1, column = 1)
tk.Button(root, text="삼겹살 도시락   [5000원]", bg = "white", fg = "black", font=("맑은 고딕", 11, "bold"), command=lambda: {add1('삼겹살 도시락'), increase_counter1('삼겹살 도시락')}, width=20).grid(row=2, column = 1)
tk.Button(root, text="닭갈비 도시락   [4500원]", bg = "black", fg = "white", font=("맑은 고딕", 11, "bold"), command=lambda: {add1('닭갈비 도시락'), increase_counter1('닭갈비 도시락')}, width=20).grid(row=3, column = 1)
tk.Button(root, text="스팸마요 컵밥   [3000원]", bg = "white", fg = "black", font=("맑은 고딕", 11, "bold"), command=lambda: {add1('스팸마요 컵밥'), increase_counter1('스팸마요 컵밥')}, width=20).grid(row=4, column = 1)
tk.Button(root, text="주문 취소", font=("맑은 고딕", 12, "bold"), command=btn_cancel, width=8).grid(row=5, column=0)
tk.Button(root, text="주문 완료", font=("맑은 고딕", 12, "bold"), command=btn_exit, width=8).grid(row=5, column=1)
tk.Button(root, text="저녁 예약", font=("맑은 고딕", 12, "bold"), command=btn_dinner, width=8).grid(row=5, column=2)
label1 = tk.Label(window, text = "주문 금액 : --------", width=30, height=1, fg="blue")
textarea1 = tk.Text(window, font=("맑은 고딕", 12, "bold"), bg = "black", fg = "white", highlightthickness=10, relief=SOLID, highlightbackground="white", width=30)
label1.pack()
textarea1.pack()
window.mainloop()