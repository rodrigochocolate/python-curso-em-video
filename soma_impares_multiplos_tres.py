soma = 0
cont = 0
for n in range(0, 501, 3):
    if n % 2 != 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} valores socilitados é {soma}')
