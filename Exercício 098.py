'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def contador(inicio, fim, passo):
    print('=-'* 30 )
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if passo == 0:
        print('Erro! Passo = 0 não é válido')
    else:
        caminho = inicio
        if inicio <= fim:
            while caminho <= fim:
                sleep(0.5)
                print(caminho, end=' ')
                caminho += passo
        else:
            while caminho >= fim:
                sleep(0.5)
                print(caminho, end=' ')
                caminho -= passo
        sleep(0.5)
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
