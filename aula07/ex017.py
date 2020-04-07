dias_aluguel = float(input('Por quantos dias o carro foi alugado? '))
km_rodados = float(input('Qual foi a quilometragem rodada? '))
valor_dia = 60.0
valor_km_rodado = 0.15
valor_a_pagar = (valor_dia * dias_aluguel) + (valor_km_rodado * km_rodados)
print(f'O valor a pagar é R$ {valor_a_pagar:.2f}')
