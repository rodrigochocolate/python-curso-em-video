def retornaMaior(*numeros):
    if len(numeros) == 0:
        maior = 0
    else:
        maior = numeros[0]
        for n in numeros:
            if n > maior:
                maior = n
    return maior

print(retornaMaior(4, 2, 1, 6, 10, 29, 2))
