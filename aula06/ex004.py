teste = input('Digite um valor: ')

print('O tipo primitivo desse valor é {}'.format(type(teste)))
print('Só temp espaços? {}'.format(teste.isspace()))
print('É um número? {}'.format(teste.isnumeric()))
print('É alfabético? {}'.format(teste.isalpha()))
print(('É alfanumérico? {}'.format(teste.isalnum())))
print('Está em maiúsculas? {}'.format(teste.isupper()))
print('Está em minúsculas? {}'.format(teste.islower()))
print('Está capitalizada? {}'.format(teste.istitle()))
