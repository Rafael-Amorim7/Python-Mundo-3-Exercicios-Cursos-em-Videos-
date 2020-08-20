'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear uma quantidade aleatória de números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

import random
import time

numeros_total = list()
def sorteio(* total):
    print(f'Sortenado {len(total)} valores da lista:',end=' ')
    for i, v in enumerate(total):
        num = random.randint(0,10)
        numeros_total.append(num)
        print(num, end=' ')
        time.sleep(0.5)
    print('pronto!'.upper())

def somaPares():
    pares = 0
    for i, v in enumerate(numeros_total):
        if v % 2 == 0 :
            pares += v
    print(f'Somando os valores pares de {numeros_total}, temos {pares}')
total_sorteio = list()
for i in range(random.randint(0,10)):
    total_sorteio.append(0)
sorteio(* total_sorteio)
somaPares()