n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)
print(f'A média do aluno foi de {media:.1f}')
if media < 5:
    print('REPROVADO!')
elif media < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
