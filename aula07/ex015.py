salario = float(input('Digite o valor do salario do funcionario: R$ '))
percentual_do_aumento = 0.15
salario_com_aumento = (1 + percentual_do_aumento) * salario

print(f'O salário do funcionario aumentou de R$ {salario:.2f} para R$ {salario_com_aumento:.2f}')
