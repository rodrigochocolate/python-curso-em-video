from datetime import date
ano = date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = ano - nascimento
    if  idade < 21:
        menores += 1
    else:
        maiores += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('Ao todo tivemos {} pessoas menores de idade'.format(menores))
