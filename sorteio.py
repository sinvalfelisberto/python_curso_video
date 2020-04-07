import random, time
opcao = str(input('Digite n para utilizar somente números: '))
opcao.upper()


def sorteio():
    print('Sorteando...')
    time.sleep(3)


if opcao == 'N' or opcao == 'n':
    sorteio()
    print(f'O número sorteado foi {random.randrange(0, 30)}, Parabéns!!!')
else:
    nome = ['Aline', 'Antonio', 'Jurema', 'Francisca', 'Maria']
    sorteio()
    print(f'A pessoa sorteada foi {nome[random.randrange(0, 4)]}, Parabéns!!!')
