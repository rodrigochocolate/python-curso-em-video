from math import sqrt

cat1 = float(input('Cateto 1: '))
cat2 = float(input('Cateto 2: '))
hip = sqrt(cat1 ** 2 + cat2 ** 2)

print(f'A hipotenusa do triângulo com os catetos {cat1} e {cat2} é {hip}')
