numerosExtensos = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número inteiro entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número inteiro entre 0 e 20: '))
print(f'Você digitou o número {numerosExtensos[n].upper()}')
