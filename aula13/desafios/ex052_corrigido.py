numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[1;31m{c}\033[m',end=' ')
        total += 1
    else:
        print(f'\033[1;33m{c}\033[m', end=' ')
print(f'\nO número {numero} tem {total} múltiplos!', end=' ')
if total == 2:
    print(f'Por isso ele é um número primo!')
else:
    print(f'Por isso ele não é um número primo!')