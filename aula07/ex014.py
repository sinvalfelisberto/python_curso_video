preco = float(input('Digite o valor do produto: R$ '))
desconto = 0.05
preco_com_desconto = (1 - desconto) * preco
print(f'O valor do produto é R$ {preco_com_desconto:.2f}')
