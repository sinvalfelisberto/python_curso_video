nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome.replace(" ",""))} letras')
print(f'Outra forma de dizer que seu nome tem {len(nome)-nome.count(" ")} letras usando a função len(nome) - nome.count(" ")')
primeiro_nome = nome.split()
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras.')