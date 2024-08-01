aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] < 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
    
print(f'O aluno {aluno["nome"]} está {aluno["situação"]}!')