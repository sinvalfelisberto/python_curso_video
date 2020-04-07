"""
Convertendo um valor em metro para cm e mm
"""
valor = float(input('Digite um valor: '))

centimetro = int(valor * 100)
milimetro = int(valor * 1000)

print(f'O medida de {valor} m corresponde a {centimetro}cm e {milimetro}mm!')