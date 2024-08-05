from random import shuffle

def sortear(vetor):
    shuffle(vetor)

def somarPares(vetor):
    pares = 0
    for i in vetor:
        if i % 2 == 0:
            pares += i
    return pares

numeros = [2, 4, 1, 5, 20]
sortear(numeros)
print(numeros)
print(somarPares(numeros))