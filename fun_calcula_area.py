def calculaArea(largura, altura):
    return largura * altura

altura = float(input('Altura: '))
largura = float(input('Largura: '))
area = calculaArea(altura, largura)
print(f'A área de um terreno {altura}x{largura} é de {area}m²')