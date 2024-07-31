matriz = [[], [], []]
for x, l in enumerate(matriz):
    for y in range(3):
        l.append(int(input(f'Digite um valor para [{x}, {y}]: ')))
print('-=-'*20)
for lin in matriz:
    for num in lin:
        print(f'[{num:^5}]', end='')
    print()
        