def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        print("Erro: Divisão por zero não é permitida.")


print("CALCULADORA")
print("Operações disponíveis:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


operacao = input("Digite o número da operação desejada: ")


if operacao in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))


    if operacao == '1':
        resultado = soma(num1, num2)
        print("Resultado:", resultado)
    elif operacao == '2':
        resultado = subtracao(num1, num2)
        print("Resultado:", resultado)
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
        print("Resultado:", resultado)
    elif operacao == '4':
        resultado = divisao(num1, num2)
        if resultado is not None:
            print("Resultado:", resultado)
else:
    print("Operação inválida. Por favor, escolha uma opção válida.")