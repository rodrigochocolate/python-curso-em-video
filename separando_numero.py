n = int(input('Digite um número: '))
u = int(str(n)[-1])
c = (n - n // 1000 * 1000) // 100
m = n // 1000
d = (n - m * 1000 - c * 100 - u) // 10 

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)
