"""
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(nome))
"""
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1 * n2
potencia = n1 ** n2
modulo = n1 // n2

# print('A soma vale {}.'.format(n1+n2))
print('A soma dos valores é {}, \na subtração é {}, \na multiplicação é {}, \na divisão é {:.3f}, \na potência é {} e \no módulo é {}'.format(soma, subtracao, multiplicacao, divisao, potencia, modulo))