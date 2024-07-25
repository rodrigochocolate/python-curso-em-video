palavras = (
    'APRENDER',
    'PROGRAMAR',
    'CURSO',
    'RICO',
    'GUSTAVO',
    'PROFESSOR',
    'AMIGO',
    'KAUE',
    'ORGAO',
    'GENITAL',
    'PRIQUITO'
)

for palavra in palavras:
    print(f'\nNa palavra "{palavra.capitalize()}" temos', end=' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')