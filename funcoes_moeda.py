def metade(num: float):
    return num / 2

def dobro(num: float):
    return num * 2

def aumentar(num: float, porcentagem: float):
    return num + num * porcentagem/100

def formatarDinheiro(dinheiro: float, moeda: str='R$'):
    moedaFormatada = moeda.upper() + str(round(dinheiro, 2)).replace('.', ',')
    if len(moedaFormatada[moedaFormatada.find(',')+1:]) < 2:
        moedaFormatada += '0'
    return moedaFormatada
    