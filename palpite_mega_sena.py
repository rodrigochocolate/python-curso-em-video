from random import randint
from time import sleep

print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{" SORTEANDO 10 JOGOS ":~^30}')
jogos = []
for c in range(n):
    jogos.append([])
for x, j in enumerate(jogos):
    for c in range(6):
        r = randint(1, 60)
        while r in j:
            r = randint(1, 60)
        j.append(r)
    j.sort()
    print(f'Jogo {x+1}: {j}')
    sleep(0.5)
print(f'{" BOA SORTE! ":-^30}')
