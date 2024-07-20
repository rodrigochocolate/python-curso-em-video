sexo = str(input('Informe seu sexo: [M/F] ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip()[0]
print(f'Sexo "{sexo.upper()}" registrado com sucesso.')
