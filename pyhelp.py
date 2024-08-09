def cabecalho(txt):
    tam = len(txt) + 4
    print('~'*tam)
    print(txt.center(tam))
    print('~'*tam)

while True:
    cabecalho('SISTEMA DE AJUDA PyHelp')
    inp = str(input('Função ou Biblioteca > ')).strip()
    if inp.upper() == 'FIM':
        cabecalho('ATÉ LOGO!')
        break
    cabecalho(f'Acessando o manual do comando {inp}')
    help(inp)
    