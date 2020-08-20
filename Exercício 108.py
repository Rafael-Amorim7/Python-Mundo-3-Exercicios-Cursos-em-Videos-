"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números como um valor monetário formatado.

"""

from moeda import metade, dobro, porcentoMais, moeda

p = float(input('Digite o preço em R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f"Aumentando de 10%, temos {moeda.moeda(moeda.porcentoMais(p, 10))}")

# Alterar no arquivo moeda.py criado no exercício 107:

def moeda(preco = 0, moeda = 'R$'):
    if moeda == 'R$':
        return f"{moeda}{preco:0.2f}".replace('.', ',')
    else:
        return f'{moeda}{preco:0.2f}'.replace(',', '.')