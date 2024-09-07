#Exemplo 1: Contagem regressiva

'''
    contador = 5

    while contador > 0:
        print(contador)
        contador -= 1

    print("Contagem regressiva concluída!")
'''

#Exemplo 2: Pedir senha até acertar
'''
    senha = "python123"
    entrada = ""

    while entrada != senha:
        entrada = input("Digite a senha: ")

    print("Senha correta!")
'''

#Exemplo 3 utilizando lista:
'''
    numeros = [23, 45, 12, 67, 34, 89, 21]
    i = 0
    maior_numero = numeros[0]  # Inicializa o maior número como o primeiro elemento da lista

    while i < 7:  # Sabemos que a lista tem 7 elementos
        if numeros[i] > maior_numero:
            maior_numero = numeros[i]
        i += 1

    print("O maior número na lista é:", maior_numero)
'''