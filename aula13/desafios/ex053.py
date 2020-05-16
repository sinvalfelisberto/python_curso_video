frase = str(input('Digite uma frase: ')).replace(" ","").upper()
inverso_frase = frase[::-1]
print(f'O inverso de {frase} é igual a {inverso_frase}')
if frase == inverso_frase:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
