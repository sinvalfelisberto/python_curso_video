numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 == numero2:
    print('Os valores são iguais!')
elif numero1 > numero2:
    print(f'O número {numero1}, que é o primeiro valor, é o maior!')
else:
    print(f'O número {numero2}, que é o segundo valor, é o maior!')
