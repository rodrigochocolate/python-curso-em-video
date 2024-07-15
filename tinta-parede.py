largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e uma área de {area}m².')
print(f'Para pintar sua parede você precisará de {tinta}l de tinta.')
