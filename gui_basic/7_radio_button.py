from tkinter import *
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text = "메뉴를 선텍하세요").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다.
btn_br1 = Radiobutton(root, text = "햄버거", value=1, variable=burger_var)
btn_br1.select()
btn_br2 = Radiobutton(root, text = "치즈햄버거", value=2, variable=burger_var)
btn_br3 = Radiobutton(root, text = "치킨햄버거", value=3, variable=burger_var)

btn_br1.pack()
btn_br2.pack()
btn_br3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar() # 여기에 int 형으로 값을 저장한다.
btn_d1 = Radiobutton(root, text = "콜라", value="콜라", variable=drink_var)
btn_d1.select() # 기본값 선택
btn_d2 = Radiobutton(root, text = "사이다", value="사이다", variable=drink_var)

btn_d1.pack()
btn_d2.pack()



def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 음료 중 선택된 라디오 항목의 값(value)을 출력


btn = Button(root, text = "주문", command=btncmd)
btn.pack()

root.mainloop()