from tkinter import *

root = Tk()
root.title("Minjin GUI")
root.geometry("640x480") #가로 * 세로

#비어있는 텍스트위젯
txt = Text(root, width=30, height=5)
txt.pack()

#위젯에 글자를 넣음
txt.insert(END, "글자를 입력하세요")

#한줄로 입력을 받을 때 씀, 엔터 안됨
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) #1: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())
    
    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)
    
btn = Button(root, text="클릭", command=btncmd )
btn.pack()

root.mainloop() #창이 닫히지 않도록 함