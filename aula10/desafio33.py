numero_01 = int(input('Digite o 1o número: '))
numero_02 = int(input('Digite o 2o número: '))
numero_03 = int(input('Digite o 3o número: '))

if (numero_01 < numero_02) and (numero_01 < numero_03):
    menor = numero_01
    if numero_03 > numero_02:
        maior = numero_03
    else:
        maior = numero_02
elif numero_02 < numero_01 and numero_02 < numero_03:
    menor = numero_02
    if numero_01 > numero_03:
        maior = numero_01
    else:
        maior = numero_03
else:
    menor = numero_03
    if numero_01 > numero_02:
        maior = numero_01
    else:
        maior = numero_02
print(f'O menor número foi {menor} e o maior foi {maior}.')