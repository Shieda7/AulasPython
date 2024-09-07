class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        
marca = input('Qual a marca do carro? ')
modelo = input('Qual o modelo do carro? ')
cor = input('Qual a cor do carro? ')
        
c1 = Carro(marca, modelo, cor)
print(c1.marca)
print(c1.modelo)
print(c1.cor)

marca = input('Qual a marca do carro? ')
modelo = input('Qual o modelo do carro? ')
cor = input('Qual a cor do carro? ')

c2 = Carro(marca, modelo, cor)
print(c2.marca)
print(c2.modelo)
print(c2.cor)