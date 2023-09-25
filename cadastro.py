import tkinter as tk
from tkinter import *
import mysql.connector

# Função para inserir dados no banco de dados
def enviar_dados():
    # Obtenha os valores das duas entradas
    valor1 = nfe.get()
    valor2 = key.get()

def mostrar_opcao(opcao_selecionada):
    label.config(text=f"Opção selecionada: {opcao_selecionada}")

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
valores = (valor1, valor2, opcao_selecionada)

cursor.execute(consulta, valores)

# Feche o cursor e a conexão
cursor.close()
conexao.close()

    # Limpe as entradas após o envio
nfe.delete(0, tk.END)
key.delete(0, tk.END)


janela = tk.Tk()
janela.title("Cadastro de KEYS")
janela.geometry("800x600")


#Var Opções
opcao_var = tk.StringVar()

#Textos
textcad = Label(janela, text="Cadastro de Keys/NFE", font=("Times", 15))
textcad.place(x=300,y=0)
txtnfe= Label(janela, text="NFE", font=("Times", 12))
txtnfe.place(x=0,y=37)
txtkey= Label(janela, text="KEY", font=("Times", 12))
txtkey.place(x=130,y=37)

label= Label(janela, text="KEY", font=("Times", 12))
label.place(x=130,y=100)

#Entrada de Dados
key = Entry(janela)
key.place(x=40,y=40, width=80)
nfe = Entry(janela)
nfe.place(x=180,y=40, width=120)


#Options
opcoes = ["Windows", "Office"]
opcao_menu = OptionMenu(janela, opcao_var, *opcoes, command=mostrar_opcao)
opcao_menu.place(x=299,y=39, width=50, height=20)

#Botões
btnEnviar = Button(janela, text="Inserir", command=enviar_dados)
btnEnviar.place(x=50,y=70, width=200)


janela.mainloop()