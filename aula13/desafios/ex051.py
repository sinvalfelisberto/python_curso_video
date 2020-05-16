primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = []
for c in range(primeiro_termo, (primeiro_termo+(10 * razao)), razao):
    termos.append(c)
for i in range(0, 10):
    print(f'{i + 1}º termo: {termos[i]}')
