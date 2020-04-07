frase = str(input('Digite sua frase: ')).strip().lower()
print(f'A letras A aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na {(frase.find("a")) + 1}ª posição.')
print(f'A última letra A apareceu na {frase.rfind("a") + 1}ª posição.')
