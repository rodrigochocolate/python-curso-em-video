distancia = int(input('Distancia da viagem (Km)? '))
if distancia > 200:
    custo = 0.45 * distancia
else:
    custo = 0.50 * distancia
print(f'O custo da viagem será de R${custo:.2f}!')
