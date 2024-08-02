jogador = {'nome': str(input('Nome do Jogador: ')).title(), 'gols': [], 'total': 0}
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, partidas):
    jogador['gols'].append(int(input(f'    Quantos gols na partida {c+1}? ')))
jogador['total'] = sum(jogador['gols'])
print('-=-'*10)
print(jogador)
print('-=-'*10)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=-'*10)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador['total']}')