lista = list()
while len(lista) < 5:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor já está na lista! Tente novamente...')
        continue
    if len(lista) == 0 or n > max(lista):   
        lista.append(n) # Último item
        print('Adicionado ao final da lista...')
    else:
        for pos, item in enumerate(lista):
            if n < item:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
print('-=-'*10)
print(lista)