'''

'''

def notas(* n, situação = False):
    '''
    --> Função para analisar notas e  situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita n váriaveis)
    :param sit:Valor opcional para indicar a situação do aluno
    :return: Retorna um dicionario com todas as informações do aluno
    '''
    media = sum(n) / len(n)
    notas = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': f'{media:0.2f}'}
    if 0 <= media < 6 and situação:
        notas ['situação'] = 'Ruim'
    elif 7 < media <= 10 and situação:
        notas ['situação'] = 'Bom'
    elif 6 <= media <= 7 and situação:
        notas ['situação'] = 'Razoavel'
    return notas

resp = notas(5.5, 8.5, 7, 10, situação = True)
for k, c in resp.items():
    print(f'{k}: {c}')
help(notas)