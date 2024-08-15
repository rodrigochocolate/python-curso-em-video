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
    