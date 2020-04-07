from math import pow
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
#tanto faz altura em centimetros ou metros
if altura > 3:
    altura /= 100.0

imc = peso / (pow(altura, 2))

if imc < 18.5:
    print(f'\033[1m\033[7;31mIMC: {imc:.2f} Você está abaixo do peso ideal!\033[m')
elif imc < 25.1:
    print(f'\033[1m\033[7;32mIMC: {imc:.2f} Você está no seu peso ideal!\033[m')
elif imc < 30.1:
    print(f'\033[1m\033[7;34mIMC: {imc:.2f} Você está com sobrepeso, cuidado!\033[m')
elif imc < 40.1:
    print(f'\033[1m\033[7;33mIMC: {imc:.2f} Você está acima do seu peso, muito cuidado! Obesidade!\033[m')
else:
    print(f'\033[1m\033[7;31mIMC: {imc:.2f} Você está muito acima do seu peso, emergência! Obesidade Mórbida\033[m')
