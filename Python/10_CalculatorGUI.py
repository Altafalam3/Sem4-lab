from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_add():
    first = e.get()
    global fnum
    fnum = float(first)
    global math
    math = "addition"
    e.delete(0,END)

def button_sub():
    first = e.get()
    global fnum
    fnum = float(first)
    global math
    math = "subtraction"
    e.delete(0,END)
def button_mul():
    first = e.get()
    global fnum
    fnum = float(first)
    global math
    math = "multiplication"
    e.delete(0,END)
def button_div():
    first = e.get()
    global fnum
    fnum = float(first)
    global math
    math = "division"
    e.delete(0,END)
def button_clear():
    e.delete(0,END)

def button_equal():
    snum = float(e.get())
    e.delete(0,END)
    if math == "addition":
        answer = fnum + snum
        e.insert(0,f"{fnum}+{snum}={answer}")
    elif math == "subtraction":
        answer = fnum - snum
        e.insert(0,f"{fnum}-{snum}={answer}")
    elif math == "multiplication":
        answer = fnum * snum
        e.insert(0,f"{fnum}x{snum}={answer}") 
    elif math == "division":
        answer = fnum / snum
        e.insert(0,f"{fnum}/{snum}={answer}")           
    else:
        e.insert(0,"Math Error")  

def butn_end():
    exit()
root= Tk()
root.title("Simple Calculator-Python")
# root.geometry("330x500")
# root.resizable(0,0)

e = Entry(root,borderwidth=5,width=65)
e.grid(row=0,column=0,columnspan=4,padx=5,pady=10)

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1),font=12)
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2),font=12)
button_3 = Button(root,text="3",padx=44,pady=20,command=lambda: button_click(3),font=12)
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4),font=12)
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5),font=12)
button_6 = Button(root,text="6",padx=44,pady=20,command=lambda: button_click(6),font=12)
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7),font=12)
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8),font=12)
button_9 = Button(root,text="9",padx=44,pady=20,command=lambda: button_click(9),font=12)
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0),font=12)

btn_add = Button(root,text="*",padx=42,pady=20,command=button_mul,font=12)
btn_sub = Button(root,text="-",padx=44,pady=20,command=button_sub,font=12)
btn_div = Button(root,text="/",padx=40,pady=20,command=button_div,font=12)
btn_mul = Button(root,text="+",padx=42,pady=20,command=button_add,font=12)
btn_equal = Button(root,text="=",padx=42,pady=20,command=button_equal,font=12)
btn_clear = Button(root,text="Clear",padx=20,pady=20,command=button_clear,font=8)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_0.grid(row=4,column=0)

btn_add.grid(row=1,column=3)
btn_sub.grid(row=2,column=3)
btn_mul.grid(row=3,column=3)
btn_div.grid(row=4,column=3)
btn_clear.grid(row=4,column=1)
btn_equal.grid(row=4,column=2)


root.mainloop()
