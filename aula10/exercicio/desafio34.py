salario = float(input('Digite o salário do funcionário: '))
faixa_corte = 1250.00
aumenta_maior_salario = 1.1
aumenta_menor_salario = 1.15
if salario > faixa_corte:
    print('salario acima da faixa de corte')
    salario = salario * aumenta_maior_salario
else:
    salario = salario * aumenta_menor_salario
print(f'O valor do salário reajustado é: R$ {salario:.2f}.')
