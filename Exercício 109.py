"""
Exercício Python 109: Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor retornado por
las vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

# Alterar no arquivo moeda.py criado no exercício 107

def dobro(numemo, formato = False):
    return (numemo*2) if formato is False else moeda(numemo*2)

def triplo(numero, formato = False):
    return (numero*3) if formato is False else moeda(numero*3)

def metade(numero, formato = False):
    return (numero/2) if not formato else moeda(numero/2)

def porcentoMais(numero, taxa, formato = False):
    desconto = numero + (numero * (taxa / 100))
    return desconto if not formato else moeda(desconto)

def porcentoMenos(numero, taxa, formato = False):
    desconto = numero - (numero * (taxa / 100))
    return desconto if not formato else moeda(desconto)