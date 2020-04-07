import math

angulo = float(input('Digite o valor do ângulo: '))
angulo_radiano = math.radians(angulo)
print(f'O ângulo de {angulo}° tem o seno de {math.sin(angulo_radiano):.2f}')
print(f'O ângulo de {angulo}° tem o cosseno de {math.cos(angulo_radiano):.2f}')
print(f'O ângulo de {angulo}° tem o tangente de {math.tan(angulo_radiano):.2f}')
