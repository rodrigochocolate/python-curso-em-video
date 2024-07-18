casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos irá pagar? R$'))
prestacao_mensal = casa / (anos * 12)

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação mensal será de R${prestacao_mensal:.2f}')

if prestacao_mensal > 0.30 * salario:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO ACEITO!')
