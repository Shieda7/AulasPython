# Desafio: Contar Vogais em uma Palavra

# Descrição: 
    # Peça ao aluno para criar um programa em Python que conte o número de vogais
    #  em uma palavra fornecida pelo usuário. 

# O programa deve:
    # Solicitar ao usuário que insira uma palavra.
    # Usar um laço for para percorrer cada letra da palavra.
    # Verificar se a letra é uma vogal (a, e, i, o, u).
    # Contar quantas vogais existem na palavra.
    # Exibir o número total de vogais na palavra.

# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Inicializa o contador de vogais
contador_vogais = 0

# Define as vogais
vogais = "aeiou"

# Usa um laço for para percorrer cada letra da palavra
for letra in palavra.lower():
    if letra in vogais:
        contador_vogais += 1

# Exibe o número total de vogais
print("A palavra contém", contador_vogais, "vogais.")
