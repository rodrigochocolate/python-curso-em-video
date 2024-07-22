numero = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
contador = 1
maior = menor = total = numero
while continuar == 'S':
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    total += numero
    contador += 1
media = total / contador
print(f'Você digitou {contador} número(s) e a média deles foi de {media}')
print(f'O maior valor foi {maior} e menor foi {menor}')
