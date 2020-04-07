# fatiamento
frase = 'Curso em Vídeo Python'
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

# Transformação

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase_02 = '   Aprenda Python       '
print(frase_02.strip())

# Divisão
string_nova = frase.split()
print(string_nova)

# Junção

print('-'.join(string_nova))
print('-'.join(frase))