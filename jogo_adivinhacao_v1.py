from time import sleep
from random import randint

print('\033[33m-=-\033[m' * 20)
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
numero = randint(0, 5)
chute = int(input('Em que número pensei? '))
print('\033[0;35mPROCESSANDO...\033[m')
sleep(1.5)
print('\033[1;32mPARABÉNS, VOCÊ ACERTOU!\033[m' if chute == numero else f'\033[1;31mERROU, ERA {numero} OTÁRIO!\033[m   ')
