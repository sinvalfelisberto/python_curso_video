
nome = str(input('Qual o seu nome? '))
valor_casa = float(input('Digite o valor da casa que deseja comprar: '))
anos = int(input('Em quantos anos deseja pagar? '))
salario = float(input('Qual o seu salario bruto? '))

prestacao = (valor_casa / (anos * 12))
print(f'prestação = R$ {prestacao:.2f}, margem = R$ {(salario * 0.30):.2f}')

if prestacao <= salario * 0.3:
    print(f'Seu emprestimo foi aprovado, {nome}! Você pagará {anos * 12} prestações no valor de R$ {prestacao:.2f}')
else:
    print(f'Empréstimos não aprovado. Prestação de R$ {prestacao:.2f} ultrapassa sua margem para empréstimos.')
