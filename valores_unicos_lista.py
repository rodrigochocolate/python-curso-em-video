lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=-'*10)
print(sorted(lista))