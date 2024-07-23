print('=' * 30)
print(f'{"CAIXA ELETRÔNICO":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? '))
ced50 = valor // 50
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
    valor -= ced50 * 50
ced20 = valor // 20
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
    valor -= ced20 * 20
ced10 = valor // 10
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
    valor -= ced10 * 10
ced01 = valor // 1
if ced01 > 0:
    print(f'Total de {ced01} cédulas de R$1')
    valor -= ced01
print('=' * 30)
print('Volte sempre! Tenha um bom dia!')
