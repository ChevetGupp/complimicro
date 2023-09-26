import tkinter as tk
from tkinter import *
import mysql.connector


def enviar_dados():
    # Obtenha os valores das duas entradas
    valor1 = winnfe.get()
    valor2 = winkey.get()
    teste3 = windows["text"]

    # Conecte-se ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastro"
    )

    cursor = conexao.cursor()

    # Execute a consulta SQL para inserir dados nas colunas do banco de dados
    consulta = "INSERT INTO teste (nfe, chave, tipo) VALUES (%s, %s, %s)"
    valores = (valor1, valor2, teste3)

    cursor.execute(consulta, valores)

    # Commit das mudanças no banco de dados
    conexao.commit()

    # Feche o cursor e a conexão
    cursor.close()
    conexao.close()

    # Limpe as entradas após o envio
    winnfe.delete(0, tk.END)
    winkey.delete(0, tk.END)


janela = tk.Tk()
janela.title("Cadastro de KEYS")
janela.geometry("800x600")


#Var Opções
opcao_var = tk.StringVar()

#Textos
textcad = Label(janela, text="Cadastro de Keys/NFE", font=("Times", 15))
textcad.place(x=300,y=0)

windowsnfe= Label(janela, text="NFE", font=("Times", 12))
windowsnfe.place(x=0,y=37)

windowskey= Label(janela, text="KEY", font=("Times", 12))
windowskey.place(x=130,y=37)

windows= Label(janela, text="Windows", font=("Times", 12))
windows.place(x=310,y=37)

label= Label(janela, text="", font=("Times", 12))
label.place(x=130,y=100)

officenfe = Label(janela, text="KEY", font=("Times", 12))
officenfe.place(x=0, y=70)

officekey= Label(janela, text="KEY", font=("Times", 12))
officekey.place(x=130,y=70)

office= Label(janela, text="Office", font=("Times", 12))
office.place(x=310,y=70)

computador= Label(janela, text="Computador", font=("Times", 12))
computador.place(x=0,y=100)

#Entrada de Dados
winkey = Entry(janela)
winkey.place(x=40,y=40, width=80)

winnfe = Entry(janela)
winnfe.place(x=180,y=40, width=120)

offkey = Entry(janela)
offkey.place(x=40,y=70, width=80)

offkey = Entry(janela)
offkey.place(x=180,y=70, width=120)

offkey = Entry(janela)
offkey.place(x=110,y=100, width=120)

#Opções
#opcoes = ["Windows", "Office"]
#opcao_menu = OptionMenu(janela, opcao_var, *opcoes)
#opcao_menu.place(x=299,y=39, width=50, height=20)

#Botões
btnEnviar = Button(janela, text="Inserir", command=enviar_dados)
btnEnviar.place(x=50,y=200, width=200)


janela.mainloop()