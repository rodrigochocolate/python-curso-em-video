def notas(*n, sit=False):
    """
    -> Função para analisar notas e a situação de um aluno
    :param n: uma ou mais notas
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: retorna um dicionário com várias informações sobre o aluno
    """
    
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n) / len(n)
    if sit:
        if dic['média'] < 5:
            dic['situação'] = 'RUIM'
        elif dic['média'] < 8:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'BOA'
            
    return dic


print(notas(4, 10, 10, 9))
help(notas)
