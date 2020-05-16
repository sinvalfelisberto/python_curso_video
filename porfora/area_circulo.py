class constantes:
    valor_pi = 3.1415

radius_value = float(input('Digite o valor do raio do círculo: '))

area = constantes.valor_pi * radius_value ** 2
print(f'O valor da área é: {area:.1f}')
