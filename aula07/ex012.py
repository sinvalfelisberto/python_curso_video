"""
conversor de moeda
"""
valor = float(input('Digite quanto você possui: R$ '))
cotacao_dollar = float(input('Quanto o dollar vale hoje? R$ '))

print(f'O valor de R${valor:.2f} convertido fica US${(valor / cotacao_dollar):.2f}')
