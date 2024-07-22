print('-' * 30)
print('Sequência de Fibonacci'.center(30))
print('-' * 30)

c = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

while c > 0:
    print(t1, end=' → ')
    t1 = t2 - t1
    t2 = t2 + t1
    c -= 1
    
print('FIM!')
