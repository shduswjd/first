from tkinter import *
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요.")

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
# variable = : 체크 박스를 눌렀을때의 값
# chkbox.select() # 자동으로 선택 처리
# chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 =Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크 해제 1: 체크
    print(chkvar2.get())

btn = Button(root, text = "click", command=btncmd)
btn.pack()

root.mainloop()