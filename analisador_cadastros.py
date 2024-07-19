total = 0
maiorH = 0
mm20 = 0
nomeH = ''

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        if idade > maiorH:
            maiorH = idade
            nomeH = nome
    elif sexo == 'F':
        if idade < 20:
            mm20 += 1
    total += idade
    

media = total / 4
print(f'A média da idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maiorH} anos e se chama {nomeH}')
print(f'Ao todo são {mm20} mulheres com menos de 20 anos')
