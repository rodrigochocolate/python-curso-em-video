print('=' * 30)
print(f'{"CAIXA ELETRÔNICO":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? '))
cedulas = 0
cedula = 100
while True:
    if valor >= cedula:
        valor -= cedula
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Total de {cedulas} de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        cedulas = 0
        if valor == 0:
            break