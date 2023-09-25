from functools import partial
import tkinter as tk
from tkinter import *

def button1(btn):
    txt["text"] = d1.get()

window = tk.Tk()

window.title("Teste")
window.geometry("600x400")

#Botões
bt1 = Button(window, width=20, text="Botão 1")
bt1["command"] = partial(button1, bt1)
bt1.place(x=200,y=100)

#Entrada de dados
d1 = Entry(window)
d1.place(x=200,y=200)


bt2 = Button(window, width=20, text="Botão 2")
bt2["command"] = partial(button1, bt2)
bt2.place(x=200,y=150)

#Textos
txt = Label(window, text="Ola Mundo")
txt.place(x=200,y=70)

window.mainloop()