const = True
while const:
    numero = int(input('Digite um número: '))
    if numero < 0:
        const = False
    else:
        cont = 0
        for c in range(1, numero + 1):
            if numero % c == 0:
                cont += 1
        if cont <= 2:
            print(f'O número número {numero} é primo.')
        else:
            print(f'O número {numero} não é primo.')
    print('-----------/*\-----------')
print('--> Fim do Programa <--')