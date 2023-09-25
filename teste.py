import tkinter as tk
from tkinter import *
from functools import partial

janela = tk.Tk()
janela.geometry("800x600")

def button(btn):
    txt["text"] = btn["text"]

btn1 = Button(janela, width=13, text="Botão 1")
btn1["command"] = partial(button, btn1)
btn1.place(x=100,y=100)

txt = Label(janela, text="Ola")
txt.place(x=100,y=70)

janela.mainloop()
