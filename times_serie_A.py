times = 'Flamengo', 'Palmeiras', 'São Paulo', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Fluminense', 'Grêmio', 'Fortaleza', 'Internacional', 'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Atlético-GO', 'Cuiabá', 'Vasco', 'Juventude', 'Criciúma', 'Vitória'
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'Corinthians está na posição: {times.index('Corinthians') + 1}')
