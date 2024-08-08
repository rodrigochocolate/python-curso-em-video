def leiaInt(texto):
    num = str(input(texto))
    while not num.isnumeric():
        print('ERRO! Digite um número inteiro válido!')
        num = str(input(texto))
    num = int(num)
    return num


n = leiaInt('Número: ')
print(type(n))