'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
def escreva(msg):
    tamanho = len(msg) + 4
    print('~'* tamanho)
    print(f'{msg.center(tamanho)}')
    print('~' * tamanho)

escreva('Guanabara')
escreva('OLÁ, MUNDO!')
escreva('MEE')