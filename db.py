import tkinter as tk
import mysql.connector

# Função para inserir dados no banco de dados
def enviar_dados():
    # Obtenha os valores das duas entradas
    valor1 = entrada1.get()
    valor2 = entrada2.get()

    # Conecte-se ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastro"
    )

    cursor = conexao.cursor()

    # Execute a consulta SQL para inserir dados nas colunas do banco de dados
    consulta = "INSERT INTO cad (NFE, chave) VALUES (%s, %s)"
    valores = (valor1, valor2)

    cursor.execute(consulta, valores)

    # Feche o cursor e a conexão
    cursor.close()
    conexao.close()

    # Limpe as entradas após o envio
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)

# Crie uma janela tkinter
janela = tk.Tk()
janela.geometry("200x100")
janela.title("Formulário de Envio")

# Crie duas entradas
entrada1_label = tk.Label(janela, text="NFE")
entrada1_label.grid(row=0,column=0)
entrada1 = tk.Entry(janela)
entrada1.grid(row=0,column=1)

entrada2_label = tk.Label(janela, text="Valor 2:")
entrada2_label.grid(row=1,column=0)
entrada2 = tk.Entry(janela)
entrada2.grid(column=1,row=1)

# Crie um botão para enviar os dados
botao_enviar = tk.Button(janela, text="Enviar Dados", command=enviar_dados)
botao_enviar.grid(row=2,column=1)

# Inicie o loop principal do tkinter
janela.mainloop()
