import math

def calcular_area_circulo(raio):
    """Calcula a área de um círculo."""
    return math.pi * (raio ** 2)

def calcular_area_retangulo(comprimento, largura):
    """Calcula a área de um retângulo."""
    return comprimento * largura

def calcular_area_triangulo(base, altura):
    """Calcula a área de um triângulo."""
    return 0.5 * base * altura

def main():
    print("Calculadora de Áreas de Formas Geométricas")
    print("Escolha uma forma geométrica:")
    print("1. Círculo")
    print("2. Retângulo")
    print("3. Triângulo")

while True:   
    escolha = int(input("Digite o número da forma desejada: "))
    
    if escolha == 1:
        raio = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(raio)
        print(f"A área do círculo é: {area:.2f}")
    
    elif escolha == 2:
        comprimento = float(input("Digite o comprimento do retângulo: "))
        largura = float(input("Digite a largura do retângulo: "))
        area = calcular_area_retangulo(comprimento, largura)
        print(f"A área do retângulo é: {area:.2f}")
    
    elif escolha == 3:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"A área do triângulo é: {area:.2f}")
    
    else:
        print("Opção inválida. Por favor, escolha um número entre 1 e 3.")


main()
