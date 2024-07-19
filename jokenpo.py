from random import randint

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = jokenpo[randint(0, 2)]
opcao = int(input('Qual é a sua jogada? '))
if opcao > 2 or opcao < 0:
    print('Digite certo...')
else:
    jogador = jokenpo[opcao]
    print('-=-' * 10)
    print('Computador jogou', computador)
    print('Jogador jogou', jogador)
    print('-=-' * 10)
    if jogador == computador:
        print('EMPATE!')
    elif jogador == 'PEDRA' and computador == 'PAPEL' or jogador == 'PAPEL' and computador == 'TESOURA' or jogador == 'TESOURA' and computador == 'PEDRA':
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADOR VENCEU!')
