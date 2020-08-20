'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa
que importe esse módulo e use algumas dessas funções.
'''

from moeda import metade, dobro, porcentoMais

p = float(input('Digite o preço em R$'))
print(f'A metade de R${p} é {metade(p)}')
print(f'O dobro de R${p} é {dobro(p)}')
print(f"Aumentando de 10%, temos R${porcentoMais(p, 10 )}")


# Criar arquivo moeda.py:

def dobro(numemo):
    return (numemo*2)

def triplo(numero):
    return (numero*3)

def metade(numero):
    return (numero/2)

def porcentoMais(numero, taxa):
    desconto = numero + (numero * (taxa / 100))
    return desconto

def porcentoMenos(numero, taxa):
    desconto = numero - (numero * (taxa / 100))
    return desconto