ano = int(input('Qual ano desejas analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO') 
