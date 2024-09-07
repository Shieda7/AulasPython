class Aluno:
    def __init__(self, nome, idade, nota, media):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.media = media
        
print('-------------------')
nome = str(input('Qual o nome do aluno? '))
idade = int(input('Qual a idade do aluno? '))
n1 = float(input('Qual foi a nota do primeiro bimestre? '))
n2 = float(input('Qual foi a nota do segundo bimestre? '))
n3 = float(input('Qual foi a nota do terceiro bimestre? '))
n4 = float(input('Qual foi a nota do quarto bimestre? '))
nota = n1+n2+n3+n4
media = nota/4

a1 = Aluno(nome, idade, nota, media)
print(f'------Aluno 1------\nNome: {a1.nome} \nIdade: {a1.idade} \nNota total: {a1.nota} \nMedia: {a1.media}')

print('-------------------')
nome = str(input('Qual o nome do aluno? '))
idade = int(input('Qual a idade do aluno? '))
n1 = float(input('Qual foi a nota do primeiro bimestre? '))
n2 = float(input('Qual foi a nota do segundo bimestre? '))
n3 = float(input('Qual foi a nota do terceiro bimestre? '))
n4 = float(input('Qual foi a nota do quarto bimestre? '))
nota = n1+n2+n3+n4
media = nota/4

a2 = Aluno(nome, idade, nota, media)
print(f'------Aluno 2------\nNome: {a2.nome} \nIdade: {a2.idade} \nNota total: {a2.nota} \nMedia: {a2.media}')
