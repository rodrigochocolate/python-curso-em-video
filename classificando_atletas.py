from datetime import date

nascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos.')

if idade <= 9:
    print(f'O atleta com {idade} anos é MIRIM!')
elif idade <= 14:
    print(f'O atleta com {idade} anos é INFANTIL!')
elif idade <= 19:
    print(f'O atleta com {idade} anos é JUNIOR!')
elif idade <= 25:
    print(f'O atleta com {idade} anos é SÊNIOR!')
else:
    print(f'O atleta com {idade} anos é MASTER!')
