jogadores = list()
while True:
    dados = dict()
    dados['nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    dados['gols'] = []
    for c in range(partidas):
        dados['gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
    continuar = str(input('Quer continuar? (S/N) ')).strip().upper()
    while continuar not in 'SN':
        print('ERRO! Apenas responda S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        
    jogadores.append(dados)
    if continuar == 'N':
        break
print('-='*30)
print(f'{"cod":<4}{"nome":<20}{"gols":<20}{"total"}')
print('-'*60)
for c in range(len(jogadores)):
    print(f'{c:<4}{jogadores[c]['nome']:<20}{str(jogadores[c]['gols']):<20}{sum(jogadores[c]['gols'])}')
while True:
    print('-'*60)
    c = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if c == 999:
        break
    elif c >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {c}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[c]['nome']}')
        for i, g in enumerate(jogadores[c]['gols']):
            print(F'    No jogo {i+1} fez {g} gols.')