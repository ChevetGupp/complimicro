#============================
#======== Cadastro ==========
#============================
import tkinter as tk
from tkinter import *

def bt_click():
    print("bt_click")

    lb["text"] = "Funcionou"


janela = tk.Tk()
janela.title("Cadastro")
#cor de fundo da janela
janela["bg"] = "black"
janela["background"] = "black"

lb = Label(janela, text="Cadastro de NFE")
lb.place(x=100,y=100)
lb["bg"] = "Black"


bt = Button(janela, width=10, text="Ok", command=bt_click)
bt.place(x=100,y=150)

janela.geometry("800x600")



janela.mainloop()