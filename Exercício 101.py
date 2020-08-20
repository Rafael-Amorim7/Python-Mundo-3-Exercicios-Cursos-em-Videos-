'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(ano):
    from datetime import date # Economiza memoria se vc importar dentro da def
    idade = (date.today().year) - ano
    print(f'Com {idade} anos:', end= ' ')
    if  idade >= 18 and idade <= 65:
        print('VOTO OBRIGATÓRIO.')
    elif idade >= 16:
        print('VOTO OPCIONAL.')
    else:
        print('NÃO VOTA.')

print('='*30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
