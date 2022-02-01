from tkinter import *
from tkinter import font
import tkinter.ttk as ttk

root = Tk()
root.title("Joystick control")
root.geometry('1000x480')
root.resizable(True, True)

# label 1 = text for "ip"
lb_ip = Label(root, text='IP', font=('AppleGothic', 30)) # 폰트 크기만 변경이 안됨..어떤 폰트랑 같이 할건지 알아야함
# lb_ip.grid(row=0, column=0) # grid 할때 pack 안써도 되
lb_ip.place(x=30, y=30) # place 쓸 때 pack 안써도 되

# entry 1 = showing ip address
en_ip = Entry(root, width = 20)
en_ip.place(x = 70, y = 50)

# label 2 = text for "port"
lb_port = Label(root, text='Port', font=('AppleGothic', 30))
lb_port.place(x = 300, y = 30)

# entry 2 = showing port number
en_port = Entry(root, width = 20)
en_port.place(x = 370, y = 50)

# button = click and showing ip address, port num
def btn_click():
    en_port.insert(0, "8000")

btn = Button(root, text = 'Click', width=10, command=btn_click)
btn.place(x=600, y = 50)

# textbox = showing message
# txtbox = Text(root, )


root.mainloop()