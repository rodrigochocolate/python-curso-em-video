from datetime import date

nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {ano}')
if idade < 18:
    print(f'Faltam {18-idade} ano(s) para seu alistamento que será em {nascimento+18}')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s) atrás que foi em {nascimento+18}')
else:
    print(f'Você já tem {idade} ano(s) e deve se alistar imediatamente!')