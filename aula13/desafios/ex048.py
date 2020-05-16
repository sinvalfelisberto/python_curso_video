soma = 0
quant = 0
for c in range(1, 501, 1):
    if c % 2 != 0:
        if c % 3 == 0:
            quant += 1
            soma += c
print(f'A soma de todos os {quant} valores solicitados é igual a {soma}.')
