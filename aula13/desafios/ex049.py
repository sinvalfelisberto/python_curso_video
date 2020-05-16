from time import sleep

print('*-' * 10)
print('   Tabuada   ')
print('*-' * 10)
print('*-' * 10)
valor = int(input('Digite a tabuada que deseja calcular: '))
for c in range(0, 11):
    resultado = valor * c
    print(f'{valor} x {c} = {resultado}')
    sleep(0.5)
print('*-' * 10)
print('Fim')