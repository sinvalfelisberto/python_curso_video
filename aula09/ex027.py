valor = int(input('Digite um valor: '))
unidade = valor // 1 % 10
dezena = valor // 10 % 10
centena = valor // 100 % 10
milhar = valor // 1000 % 10
print(f'Analisando o {valor}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
