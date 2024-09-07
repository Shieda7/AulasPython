#area = 3.14*raio*raio
class Circulo:
    def __init__(self, raio, area):
        self.raio = raio
        self.area = area
        
raio = float(input('Qual é o raio do primeiro círculo? '))
area = 3.14 * raio * raio

c1 = Circulo(raio, area)
print(f'O raio do círculo 1 é: {c1.raio}')
print(f'E a área do círculo 1 é: {c1.area}')

raio = float(input('Qual é o raio do segundo círculo? '))
area = 3.14 * raio * raio

c2 = Circulo(raio, area)
print(f'O raio do círculo 2 é: {c2.raio}')
print(f'E a área do círculo 2 é: {c2.area}')