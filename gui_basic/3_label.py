from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Nado GUI")

label1 = Label(root, text = "안녕하세요")
label1.pack()

photo = PhotoImage(file="./img,png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") # config : 글자/사진 바꿔줌

    global photo2 # 이거 안하면 저 위에 있는 체크박스가 사라져 있음.
    photo2 = PhotoImage(file = "gui_basic/img.png")
    label2.config(image=photo2)

btn = Button(root, text='클릭', command=change)
btn.pack()


root.mainloop() #실행