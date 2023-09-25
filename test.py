import tkinter as tk

# Função para mostrar a opção selecionada
def mostrar_opcao(opcao_selecionada):
    label.config(text=f"Opção selecionada: {opcao_selecionada}")

# Crie uma janela tkinter
janela = tk.Tk()
janela.title("Rótulo de Opções")

# Crie um rótulo
label = tk.Label(janela, text="")
label.pack(pady=20)

# Crie uma variável de Tkinter para armazenar a opção selecionada
opcao_var = tk.StringVar()

# Crie um OptionMenu com algumas opções
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
opcao_menu = tk.OptionMenu(janela, opcao_var, *opcoes, command=mostrar_opcao)
opcao_menu.pack()

# Configure um botão para mostrar a opção selecionada
botao = tk.Button(janela, text="Mostrar Opção", command=lambda: mostrar_opcao(opcao_var.get()))
botao.pack()

# Inicie o loop principal do tkinter
janela.mainloop()
