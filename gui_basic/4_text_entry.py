from tkinter import *
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요.")
 
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # "1.0": 1번째 라인, 0번째 인덱스(column)부터 가져와라
    # END : 끝까지 가져와라 
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "click", command=btncmd)
btn.pack()

root.mainloop()