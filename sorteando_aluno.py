from random import randint, choice

alunos = []
numero = randint(0, 3)

for x in range(0, 4):
    alunos.append(str(input(f'{x+1}º Aluno: ')))

print('O aluno escolhido foi', alunos[numero])
print('O aluno escolhido foi', choice(alunos))
