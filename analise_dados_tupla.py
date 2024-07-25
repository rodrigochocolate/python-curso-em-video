nums = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
pares = 0
for n in nums:
    if n % 2 == 0:
        pares += 1

print(f'Você digitou os valores {nums}')
print(f'O número 9 apareceu {nums.count(9)} veze(s)')
print(f'O valor 3 apareceu na {nums.index(3) + 1}ª posição')
print(f'Os valores pares digitados foram {pares}')