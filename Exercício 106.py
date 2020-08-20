"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará. Importante: use cores aleatórias.
"""

from  random import  randint
from time import  sleep

def texto (msg, letter_color, background_color):
    tam = len(msg) + 4
    print(f'\033[1;{letter_color};{background_color}m~' *tam)
    print(f'{msg.center(tam)}'.upper())
    print('~' *tam)
    print('\033[m')
    sleep(1)


letter = background = 0

def color():
    while True:
        global letter, background
        letter = randint(30, 35)
        background = randint(40, 45)
        if letter + 10 != background and letter + 8 != background:
            break


while  True:
    color()
    texto('sistema de ajuda pyhelp', letter, background)
    func = input('Função ou Biblioteca > ')
    if func == 'exit()':
        break
    color()
    texto(f'acessando o manual do comando "{func}"', letter, background)
    print('\033[1;33;40m')
    help(func)
    sleep(1)

color()
print('Volte Sempre!')
