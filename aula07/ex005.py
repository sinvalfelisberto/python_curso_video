print('Módulo de Habitação')
meses = int(input('Digite a quantidade de meses restantes do seu contrato: '))

anos = meses // 12
restoMeses = meses % 12
if restoMeses > 0:
    print('Restam {} anos e {} meses para o fim do seu contrato!'.format(anos, restoMeses))
else:
    print('Restam {} anos para o fim do seu contrato!'.format(anos))

frutas = ['goiaba', 'banana', 'acerola']
for x in frutas:
    print(x.capitalize())
