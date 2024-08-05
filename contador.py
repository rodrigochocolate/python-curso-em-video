def contador(inicio, fim, passo):
    print('-='*15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo > 0:
        passo *= -1
    for c in range(inicio, fim+passo, passo):
        print(c, end=' ')
    print('FIM!')
    print('-='*15)

contador(1, 10, 1)
contador(10, 0, -2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)