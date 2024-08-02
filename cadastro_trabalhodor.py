from datetime import date

cadastro = {
    'nome': str(input('Nome: ')),
    'idade': date.today().year - int(input('Ano de Nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): '))
}

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratacao'] - date.today().year + cadastro['idade'] + 35
    
print('-=-'*10)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor de {v}')