import time
import tkinter.ttk as ttk  #프로그레스바, 콤보박스 사용
from tkinter import *

root = Tk()
root.title("Minjin GUI")
root.geometry("640x480") #가로 * 세로

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#    progressbar.stop() #작동 중지

# btn = Button(root, text="중지", command=btncmd )
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101): #1~ 100
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) #프로그레스 바의 값 설정
        progressbar2.update() #매번 for문 동작할때마다 ui가 업데이트 됨
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2 )
btn.pack()


root.mainloop() #창이 닫히지 않도록 함
