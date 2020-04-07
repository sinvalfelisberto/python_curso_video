"""
Retorna a hipotenusa h² = c_op² + a_adj²
"""
from math import hypot

c_oposto = float(input('Comprimento do catetos oposto: '))
c_adjacente = float(input('Comprimento do cateto adjvacente: '))
# hipotenusa = (c_oposto ** 2 + c_adjacente ** 2 ) ** (1/2)
hipotenusa = hypot(c_oposto, c_adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
