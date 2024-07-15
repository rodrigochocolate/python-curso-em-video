km_rodados = float(input('Quantos KM foram rodados? '))
dias = int(input('Por dias o carro foi usado? '))
total = km_rodados * 0.15 + dias * 60

print(f'O aluguel do carro custou R${total:.2f}')
