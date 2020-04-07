primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
media = (primeira_nota + segunda_nota) / 2.0
print(f'A sua média foi {media:.1f}')
if media >=7:
    print('Você foi aprovado!')
else:
    print('Você está reprovado!')
print('-*/-*/-*/ Fim \*-\*-\*-')
