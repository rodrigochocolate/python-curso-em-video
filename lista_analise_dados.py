pessoas = []
dados = []
pesos = []

while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    pesos.append(dados[1])
    pessoas.append(dados[:])
    dados.clear()
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? (S/N) ')).strip().upper()[0]
    if continuar == 'N':
        break    
        
mais_pesados = []
mais_leves = []
for p in pessoas:
    if p[1] == max(pesos):
        mais_pesados.append(p[0])
    if p[1] == min(pesos):
        mais_leves.append(p[0])
        
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {max(pesos)}Kg. Peso de {'; '.join(mais_pesados)}.')
print(f'O menor peso foi de {min(pesos)}Kg. Peso de {'; '.join(mais_leves)}')
