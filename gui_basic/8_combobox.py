import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Minjin GUI")
root.geometry("640x480") #가로 * 세로

values = [str(i) + "일" for i in range(1,32)] #1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, value=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 뿐 아니라 버튼 클릭을 통한 값 설정도 가능

readonly_combobox = ttk.Combobox(root, height=10, value=values, state="readonly") #읽기 전용
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
   print(combobox.get()) #선택된 값 표시
   print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd )
btn.pack()

root.mainloop() #창이 닫히지 않도록 함