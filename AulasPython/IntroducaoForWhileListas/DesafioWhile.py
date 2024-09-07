#Desafio: Jogo de Adivinhação
#Descrição: Peça ao aluno para criar um jogo de adivinhação em Python. 
# O programa deve gerar um número aleatório entre 1 e 100, e o jogador deve adivinhar qual é esse número. 
# O jogo continua até que o jogador acerte o número ou decida sair. 
# O programa deve fornecer dicas se o palpite do jogador for muito alto ou muito baixo.

import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa uma variável para armazenar o palpite do jogador
palpite = None

# Inicia o laço while
while palpite != numero_secreto:
    palpite = input("Adivinhe o número (ou digite 'sair' para encerrar): ")
    
    if palpite.lower() == "sair":
        print("Jogo encerrado. O número era:", numero_secreto)
        break
    
    # Converte o palpite para um número inteiro
    palpite = int(palpite)
    
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você adivinhou o número.")
