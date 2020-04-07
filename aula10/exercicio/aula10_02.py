# estruturas condicionais
valor = int(input('Quantos anos tem seu carro?: '))
if valor <= 3:
    print('Seu carro ainda está novo!')
else:
    print('Seu carro está velho')
print('--- Fim ---')
# outra forma de fazer uma condicional
print('Seu carro ainda está novo!' if valor <=3 else 'Seu carro está velho!')
