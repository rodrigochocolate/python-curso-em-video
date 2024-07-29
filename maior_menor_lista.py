lista = []
for c in range(5):
    n = int(input('Digite o número: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n       
        
print(lista)
a = lista.rindex(maior)
print(a)
