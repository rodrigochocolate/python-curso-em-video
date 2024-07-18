print('-=-' * 10)
print('Analisador de Triângulos'.center(30))
print('-=-' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and c + b > a:
    print(f'Os segmentos {a}, {b} e {c} podem formar um triângulo!')
else:
    print(f'Os segmentos {a}, {b} e {c} NÃO podem formar um triângulo!')
