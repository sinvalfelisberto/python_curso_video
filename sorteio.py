import random, time

def sorteio():
    print('Sorteando...')
    time.sleep(3)
cont = 0
while cont < 3:
        nome = ['Alcy', 'Alderiane', 'Aline Azevedo', 'Aline Giseli', 'Angelica', 'Bianca', 'Cesar', 'Camila', 'Bruna', 'Candida', 'CArla', 'Clea', 'Cleide', 'Cristiane', 'Dayane', 'Diene', 'Lindinalva', 'Ecelene', 'Edenise', 'Edineuma', 'Cristina', 'Elena', 'Elen', 'Elenice Araujo', 'Elenice', 'Erica', 'Fabiana', 'Fatima', 'Fernada', 'Fran', 'Gabrielly', 'Gislane', 'Helena', 'Jaqueline', 'Kelen', 'Wllanland', 'Laura', 'Leila', 'Leiliane', 'Lenita', 'Letícia', 'Lucyhelen', 'Maria Antônia', 'Catarina', 'Marilene', 'Maristela', 'Mayara', 'Meiryelen', 'Mercilene', 'Michele', 'Michele Martins', 'Monalisa', 'Neta', 'Paula', 'Pollyana', 'Rafaela', 'Rita', 'Rosangela', 'Rosi', 'Samara', 'Samira', 'Sheyla', 'Socorro', 'Tania', 'Valdir', 'Valneide', 'Vercianny', 'Vilma', 'Vivianny', 'Welita']
        sorteio()
        print(f'A pessoa sorteada foi {nome[random.randrange(0, len(nome))]}, Parabéns!!!')
        cont += 1
