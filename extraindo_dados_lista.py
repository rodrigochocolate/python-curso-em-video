valores = []
valores_decrescente = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? (S/N) ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=-' * 10)
print(f'Você digitou {len(valores)} valores')
for valor in sorted(valores):
    valores_decrescente.insert(0, valor)
print('Os valores em ordem decrescente são', valores_decrescente)
print('Os valores em ordem decrescente são', sorted(valores, reverse=True))
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontado na lista!')