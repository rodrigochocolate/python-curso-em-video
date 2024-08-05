cadastros = []
totIdade = 0
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    
    cadastros.append(dados)
    totIdade += dados['idade']
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        print('ERRO! Apenas responda S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        
    if continuar == 'N':
        break
    
print('-='*15)
media = totIdade / len(cadastros)
print(f'A) Ao todo temos {len(cadastros)} oessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in cadastros:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print('\nD) Lista de pessoas que estão acima da média:')
for c in cadastros:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<< ENCERRADO >>')