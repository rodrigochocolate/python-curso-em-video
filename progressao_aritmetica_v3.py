termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
ultimo_termo = termo + 9*razao
while termo <= ultimo_termo:
    print(termo, end=' → ')
    if termo == ultimo_termo:
        print('PAUSA')
        mais_termos = int(input('Quantos termos a mais você quer mostrar? '))
        ultimo_termo += mais_termos * razao
    termo += razao
    