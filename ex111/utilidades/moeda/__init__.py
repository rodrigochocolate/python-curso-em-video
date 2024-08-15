def metade(num: float, formatar=False):
    return formatarDinheiro(num / 2) if formatar else num / 2

def dobro(num: float, formatar=False):
    return formatarDinheiro(num * 2) if formatar else num * 2

def aumentar(num: float, porcentagem: float, formatar=False):
    return formatarDinheiro(num + num * porcentagem/100) if formatar else num + num * porcentagem/100

def formatarDinheiro(dinheiro: float, moeda: str='R$'):
    moedaFormatada = moeda.upper() + str(round(dinheiro, 2)).replace('.', ',')
    if len(moedaFormatada[moedaFormatada.find(',')+1:]) < 2:
        moedaFormatada += '0'
    return moedaFormatada
    
def cab(tam, txt):
    lin(tam)
    print(txt.center(tam))
    lin(tam)
    
def lin(tam):
    print('-' * tam)
    
def reduzir(preco: float, porcentagem: float, formatar=False):
    return formatarDinheiro(preco - preco * porcentagem/100) if formatar else preco - preco * porcentagem/100
    
def resumo(preco: float, aumento: float, reducao: float):
    cab(40, 'RESUMO DO VALOR')
    print(f'Preço analisado: {formatarDinheiro(preco)}')
    print(f'Dobro do preço: {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')
    print(f'{aumento}% de aumento: {aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: {reduzir(preco, reducao, True)}')
    lin(40)