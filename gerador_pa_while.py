print('=' * 20)
print('GERADOR PA'.center(20))
print('=' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ultimo_termo = 9*razao + termo

while termo <= ultimo_termo:
    print(termo, end=' → ')
    termo += razao

print('ACABOU!')
