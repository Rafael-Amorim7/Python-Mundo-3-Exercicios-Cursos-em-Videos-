'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''

from random import randint
from time import sleep

def maior( * total):
    maior_valor = contador = 0
    print('=-'*20)
    if  len(total) == 0:
        print('Não foi passado nenhum valor...')
    else:
        print('Analisando os valores passados...')
        for i, v in enumerate(total):
            contador = i + 1
            num = randint(0,100)
            if maior_valor < num:
                maior_valor = num
            print(num, end= ' ')
            sleep(0.3)
        print()
        print(f'Foram informados {contador} valores.\nO maior valor foi {maior_valor}')

total_sorteio = list()
for i in range(randint(0,50)):
    total_sorteio.append(0)

maior( * total_sorteio)
maior()