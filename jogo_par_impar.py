from random import randint
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))
print('-=-'*10)
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    chute = ' '
    while chute not in 'PI':
        chute = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = jogador + computador
    parOuImpar = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {parOuImpar}')
    print('-'*30)
    if chute == parOuImpar[0]:
        vitorias += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-'*30)
    else:
        print('Você PERDEU!')
        print('-=-'*10)
        break
print(f'GAME OVER! Você venceu {vitorias} veze(s)') 