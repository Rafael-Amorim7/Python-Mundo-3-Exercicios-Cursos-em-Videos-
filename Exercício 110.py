"""
Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

# Alterar no arquivo moeda.py criado no exercício 107

def resumo(preco=0, taxa=10, taxa_2=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda.preco}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxa}% de aumento: \t{porcentoMais(preco, taxa, True)}')
    print(f'{taxa_2}% de redução: \t{porcentoMenos(preco, taxa_2, True)}')
    print('-' * 30)