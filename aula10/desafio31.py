distancia_total = float(input('Digite a distância da sua viagem: '))
passagem_normal = 0.50
passagem_desconto = 0.45
if distancia_total > 200.00:
    custo_passagem = distancia_total * passagem_desconto
else:
    custo_passagem = distancia_total * passagem_normal
print(f'O valor da sua passagem é R$ {custo_passagem:.2f}')
