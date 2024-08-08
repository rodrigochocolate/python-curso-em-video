def jog(gols, nome='<desconhecido>'):
    if not gols.isnumeric():
        gols = 0
    else:
        gols = int(gols)
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gols')

nome = str(input('Nome: '))
gols = str(input('Gols: '))
jog(gols, nome)