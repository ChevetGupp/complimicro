import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import subprocess

def btnex():
    try:
        # Abre a caixa de diálogo para selecionar o arquivo .bat
        arquivo_bat = filedialog.askopenfilename(filetypes=[("Arquivos .BAT", "*.bat")])

        # Verifica se o usuário selecionou um arquivo .bat
        if arquivo_bat:
            # Use o comando 'subprocess' para executar o arquivo .bat
            subprocess.run([arquivo_bat], shell=True)
            messagebox.showerror("Erro", f"Erro ao executar o arquivo .bat: {str(e)}")

            # Exibe uma mensagem de sucesso quando o terminal é fechado
            messagebox.showinfo("Sucesso", "O terminal foi fechado com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o arquivo .bat: {str(e)}")

def janela_teste(titulo):
    janela = tk.Toplevel(root)
    janela.geometry("400x300+100+100")
    janela.title(titulo)

    btnEx = tk.Button(janela, text="Executar", command=btnex)
    btnEx.pack()

    janela.lift()


def executar_arquivo_bat(titulo):
    janela = tk.Toplevel(root)
    janela.title(titulo)
    try:
        # Abre a caixa de diálogo para selecionar o arquivo .bat
        arquivo_bat = filedialog.askopenfilename(filetypes=[("Arquivos .BAT", "*.bat")])

        # Verifica se o usuário selecionou um arquivo .bat
        if arquivo_bat:
            # Use o comando 'subprocess' para executar o arquivo .bat
            subprocess.run([arquivo_bat], shell=True)
            messagebox.showerror("Erro", f"Erro ao executar o arquivo .bat: {str(e)}")

            # Exibe uma mensagem de sucesso quando o terminal é fechado
            messagebox.showinfo("Sucesso", "O terminal foi fechado com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o arquivo .bat: {str(e)}")

root = tk.Tk()
root.geometry("400x300+100+100")
root.title("Executar Arquivo .BAT")

botao_executar = tk.Button(root, text="Janela Teste", command=lambda: janela_teste("Janela 1"))
botao_executar.pack()

root.mainloop()
