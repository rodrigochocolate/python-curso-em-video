n = int(input('Digite um número: '))
d = 0
for c in range(1, n+1):
    if n % c == 0:
        d += 1
        print(f'\033[1;32m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nO número {n} foi divísivel {d} vezes')
if d == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')