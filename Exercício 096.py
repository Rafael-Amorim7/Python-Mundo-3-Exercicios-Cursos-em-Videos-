'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(n1, n2):
    print(f'A área do terreno é {l * c} m²')

print(f'{"CONTROLE DE TERRENO":^30}')
print('-'*30)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l,c)