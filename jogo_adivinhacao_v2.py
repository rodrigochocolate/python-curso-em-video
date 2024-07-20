from random import randint
sorteado = randint(0, 10)
print('Acabei de pensar em um número inteiro entre 0 e 10. Consegue adivinhar qual foi? ')
palpite = int(input('Seu palpite: '))
cont = 1

while palpite != sorteado:
    if palpite > sorteado:
        print('MENOS...')
    elif palpite < sorteado:
        print('MAIS...')
    palpite = int(input('Seu palpite: '))
    cont += 1

print(f'Acertou com {cont} tentativa(s). Parabéns!')
