alunos = []
dados = []
while True:
    dados.append(str(input('Nome: ')).title())
    dados.append([float(input('Nota 1: ')),
                  float(input('Nota 2: '))])
    alunos.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if continuar == 'N':
        break
print('='*50)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for c, a in enumerate(alunos):
    print(f'{c:<4}{a[0]:<10}{sum(a[1])/2:>8.1f}')
while True:
    print('-'*30)   
    n = int(input('Mostrar notas de qual aluno? (-1 interrompe): '))
    if n == -1:
        break
    print(f'Notas de {alunos[n][0]}: {alunos[n][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')