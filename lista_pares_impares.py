valores = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print('Os valores pares digitados foram:', sorted(valores[0]))
print('Os valores ímpares digitados foram:', sorted(valores[1]))
