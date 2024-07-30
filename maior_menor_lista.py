lista = []
posMaior = []
posMenor = []
for c in range(5):
    n = int(input(f'Digite o número para a posição {c+1}: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
        
    elif n < menor:
        menor = n       
        
print(lista)
print(f'Maior foi {maior} nas posições ', end='')
for pos1, x in enumerate(lista):
    if x == maior:
        print(pos1+1, end='... ')
print(f'\nMenor foi {menor} nas posições ', end='')
for pos2, y in enumerate(lista):
    if y == menor:
        print(pos2+1, end='... ')