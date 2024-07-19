print('=' * 30)
print('10 TERMOS DE UMA P.A'.center(30))
print('=' * 30)
primeiro_termo = int(input('1° termo: '))
razao = int(input('Razão: '))
ultimo_termo = primeiro_termo + (10 - 1) * razao

for n in range(primeiro_termo, ultimo_termo+1, razao):
    print(n, end=' → ')
print('ACABOU!')
