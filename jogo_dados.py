from random import randint
from time import sleep

jogadores = dict()

for c in range(4):
    num = randint(1, 6)
    jogadores[f'jogador{c+1}'] = num
    print(f'Jogador {c+1} tirou {num}.')
    sleep(1)

print('-=-'*10)
print('== RANKING DOS JOGADORES ==')

for c in range(4):
    maiorDado = max(jogadores.values())
    for k, v in jogadores.items():
        if v == maiorDado:
            print(f'  {c+1}º Lugar: {k} com {v}')
            sleep(1)
            del jogadores[k]
            break
    