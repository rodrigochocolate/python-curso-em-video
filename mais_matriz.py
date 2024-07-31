matriz = [[], [], []]
soma_pares = soma_coluna3 = 0
for x, l in enumerate(matriz):
    for y in range(3):
        l.append(int(input(f'Digite um valor para [{x}, {y}]: ')))
print('-=-'*20)
for lin in matriz:
    for y, num in enumerate(lin):
        print(f'[{num:^5}]', end='')
        if num % 2 == 0:
            soma_pares += num
        if y == 2:
            soma_coluna3 += num
    print()
print('-=-'*20)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')