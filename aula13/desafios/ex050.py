def display_info():
    print('/*-' * 10)
soma = 0
cont = 0
display_info()
for c in range (1, 7):
    numero = int(input(f'Digite o {c}º número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
if cont == 1:
    print(f'Você informou {cont} número par e a soma é igual a {soma}.')
else:
    print(f'Você informou {cont} números pares e a soma é igual a {soma}.')
display_info()
