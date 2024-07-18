salario = float(input('Salário: R$'))
aumento = 15/100

if salario > 1250:
    aumento = 10/100

salario += aumento * salario
print(f'O salarío de passou a ser R${salario:.2f}')
