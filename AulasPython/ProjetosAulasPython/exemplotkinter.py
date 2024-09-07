import tkinter as tk

# Cria uma instância da classe Tk (janela principal)
root = tk.Tk()

# Define o título da janela
root.title("Minha Primeira Janela")

# Define o tamanho da janela (largura x altura)
root.geometry("300x200")

# Adiciona um rótulo (label) com um texto
label = tk.Label(root, text="Olá, Tkinter!")
label.pack(pady=20)  # Adiciona o rótulo à janela e adiciona um padding vertical

# Adiciona um botão que fecha a aplicação
button = tk.Button(root, text="Fechar", command=root.quit)
button.pack(pady=10)  # Adiciona o botão à janela e adiciona um padding vertical

# Inicia o loop principal da interface gráfica
root.mainloop()