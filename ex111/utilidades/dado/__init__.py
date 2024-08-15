def leiaDinheiro(txt):
    while True:
        dinheiro = str(input(txt)).strip().replace(',', '.')
        if dinheiro.replace('.', '').isnumeric():
            break
        print('ERRO! Digite um dinheiro válido.')
    return float(dinheiro)