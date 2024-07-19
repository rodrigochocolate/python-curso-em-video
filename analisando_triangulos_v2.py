a = float(input('1° Segmento: '))
b = float(input('2° Segmento: '))
c = float(input('3° Segmento: '))

if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO!')
    elif a == b or b == c or a == c:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES!')
    else:
        print('Os segmetnos acima podem formar um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
