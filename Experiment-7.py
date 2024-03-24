import tkinter as tk
from tkinter import*
window=tk.Tk()
window.title("Calculator")
window.geometry("320x400")

label1=Label(window,text="CALCULATOR", font=("Arial",18))
label1.place(x=75,y=10)
label2=Label(window,text="Type value 1:",font=("Arial",12))
label3=Label(window,text="Type value 2:", font=("Arial",12))
label2.place(x=30,y=60)
label3.place(x=30,y=100)


text1=IntVar()
val1=Entry(window,textvariable=text1)
val1.place(x=130,y=65)
text2=IntVar()
val2=Entry(window,textvariable=text2)
val2.place(x=130,y=105)
n1=text1.get()
n2=text2.get()

anslabel=Label(window)
anslabel.place(x=40,y=200)


def add():
    a = int(text1.get())
    b = int(text2.get())
    sol = a + b
    res.delete(0, END)
    res.insert(0, str(sol))


def sub():
    a = int(text1.get())
    b = int(text2.get())
    sol = a - b
    res.delete(0, END)
    res.insert(0, str(sol))


def mul():
    a = int(text1.get())
    b = int(text2.get())
    sol = a * b
    res.delete(0, END)
    res.insert(0, str(sol))


def div():
    a = int(text1.get())
    b = int(text2.get())
    if b != 0:
        sol = a / b
        res.delete(0, END)
        res.insert(0, str(sol))
    else:
        res.delete(0, END)
        res.insert(0, "Cannot divide by 0")

addition=Button(window,text="+",bg="green",fg="white", width=7,height=2,command=add)
addition.place(x=10,y=150)
subtraction=Button(window,text="-",bg="green",fg="white", width=7,height=2,command=sub)
subtraction.place(x=90,y=150)
multiplicaltion=Button(window,text="x",bg="green",fg="white", width=7,height=2,command=mul)
multiplicaltion.place(x=170,y=150)
division=Button(window,text="/",bg="green",fg="white", width=7,height=2,command=div)
division.place(x=250,y=150)

label4 = Label(window,text="Result:", font=("Arial",12))
label4.place(x = 75, y = 280)

res = Entry(window)
res.place(x=129, y= 285)

window.mainloop()