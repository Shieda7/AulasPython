import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Biblioteca para trabalhar com imagens

#a
# Função para verificar o palpite do jogador
def verificar_palpite():
    try:
        palpite = int(entry.get())
        if palpite == numero_correto:
            # Mostrar mensagem de vitória e imagem correspondente
            messagebox.showinfo("Parabéns!", "Você acertou!")
            mostrar_imagem("vitoria.png")  # Substitua pelo caminho da sua imagem de vitória
        else:
            # Mostrar mensagem de erro e imagem correspondente
            messagebox.showerror("Tente Novamente", "Palpite incorreto.")
            mostrar_imagem("erro.png")  # Substitua pelo caminho da sua imagem de erro
    except ValueError:
        # Mensagem de erro caso o valor não seja um número
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def mostrar_imagem(caminho_imagem):
    try:
        imagem = Image.open(caminho_imagem)
        imagem = imagem.resize((200, 200), Image.ANTIALIAS)  # Redimensiona a imagem
        imagem_tk = ImageTk.PhotoImage(imagem)
        
        # Atualiza o rótulo da imagem
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk  # Mantém uma referência da imagem
    except FileNotFoundError:
        print("Imagem não encontrada:", caminho_imagem)

# Número correto para o palpite
numero_correto = 7  # Defina o número correto aqui

# Cria a janela principal
root = tk.Tk()
root.title("Jogo de Adivinhação")

# Define o tamanho da janela
root.geometry("400x300")

# Cria a caixa de entrada para o palpite
entry = tk.Entry(root)
entry.pack(pady=20)

# Cria o botão para verificar o palpite
button = tk.Button(root, text="Verificar Palpite", command=verificar_palpite)
button.pack(pady=10)

# Cria um rótulo para exibir a imagem
label_imagem = tk.Label(root)
label_imagem.pack(pady=20)

# Inicia o loop principal da interface gráfica
root.mainloop()
