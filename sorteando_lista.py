from random import sample, shuffle

alunos = []
for x in range(0, 4):
    alunos.append(str(input(f'{x+1}° Aluno: ')))
    
print(sample(alunos, 4))
shuffle(alunos)
print(alunos)
