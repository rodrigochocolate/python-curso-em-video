valores = list()
pares = list()
impares = list()
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? (S/N) ')).upper().strip()[0]
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    if continuar == 'N':
        break
print(valores)
print(pares)
print(impares)