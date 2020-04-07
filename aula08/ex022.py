import random

nome_1 = str(input('Primeiro aluno: '))
nome_2 = str(input('Segundo aluno: '))
nome_3 = str(input('Terceiro aluno: '))
nome_4 = str(input('Quarto aluno: '))
lista = [nome_1, nome_2, nome_3, nome_4]
random.shuffle(lista)
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}!')
print(f'A ordem de apresentação será: ')
print(lista)
