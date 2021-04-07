from tkinter import *

root = Tk()
root.title("Minjin GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요~~")
label1.pack()

photo = PhotoImage(file = "gui_basic/img.png")
label2 =  Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") #글자 바꾸기

    global photo2 #전역 변수로 설정안하면 안나타남 쓰레기인줄알고 없앰!
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop() #창이 닫히지 않도록 함