frase = str(input('Digite um frase: ')).upper().strip().split()
frase_junta = ''.join(frase)
frase_junta_invertida = ''     

for c in range(len(frase_junta)-1, -1, -1):
    frase_junta_invertida += frase_junta[c]

print(f'O inverso de {frase_junta} é {frase_junta_invertida}!')
if frase_junta == frase_junta_invertida:
    print('Temos um palíndromo!')
else:
    print('NÃO temos um palíndromo!')