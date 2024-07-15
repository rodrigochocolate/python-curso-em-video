quantidade_notas = int(input('Quantas notas? '))
notas = []
total = 0

for n in range(0, quantidade_notas):
    nota = float(input(f'{n+1}ª nota: '))
    notas.append(nota)
    total += nota

media = total / (len(notas))
print(f'A média do aluno é {media}')
