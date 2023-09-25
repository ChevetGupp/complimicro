import tkinter as tk
from tkinter import *
from functools import partial

window = tk.Tk()
window.geometry("400x300")

def button():

    if(str(en1.get()).isnumeric() and str(en2.get()).isnumeric()):
        num1 = int(en1.get())
        num2 = int(en2.get())

        txt["text"] = int(num1+num2)
    else:
        txt["text"] = "Você não digitou um Numero valido"

bt1 = Button(window, width=20, text="Soma", command=button)
bt1.place(x=100,y=190)

en1 = Entry()
en1.place(x=100,y=160)
en2 = Entry()
en2.place(x=100,y=140)

txt = Label(window, text="Ola")
txt.place(x=100,y=180)


window.mainloop()