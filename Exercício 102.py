'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando
se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(numero = 1, show = False):
    '''
    --> Calcula o fatorial de um número
    :param numero: O numero a ser calculado o fatorilal
    :param show: parametro opcional para mostrar a conta
    :return: O valor do fatorial de numero
    '''
    fator = 1
    for i in range (numero, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fator *= i
    return fator
print('='*30)
print(fatorial(5, show=True))
