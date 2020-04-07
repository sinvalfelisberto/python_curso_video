import datetime, time

ano = int(input('Digite o ano que você quer verificar:(\033[7;30mDigite 0 para ano atual\033[m) '))


def esperar():
    print('\033[7;31mProcessando...\033[m')
    time.sleep(3)


if ano == 0:
    ano = datetime.date.today().year
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    esperar()
    print(f'{ano} é um Ano bissexto')
else:
    esperar()
    print(f'{ano} não é um ano bissexto!')
