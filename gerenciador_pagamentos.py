print('=' * 30)
preco = float(input('Preço total das compras: '))
print('=' * 30)
print('Como você deseja pagar?')
print('=' * 30)
print('[ 1 ] Dinheiro / Cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print('=' * 30)
opcao = int(input('Opção: '))
if opcao == 1:
    preco -= preco * 10/100
    print(f'Vai custar: R${preco:.2f}')
elif opcao == 2:
    preco -= preco * 5/100
    print(f'Vai custar: R${preco:.2f}')
elif opcao == 3:
    print(f'Vai custar: 2x de R${preco/2:.2f}')
elif opcao == 4:
    preco += preco * 20/100
    quant_parcelas = int(input('Quantas parcelas? '))
    valor_parcela = preco / quant_parcelas
    print(f'Parcelado em {quant_parcelas}x vezes, o valor da parcela é R${valor_parcela:.2f}')
    print(f'No total vai ficar R${preco:.2f}')
else:
    print('Digite certo amigo...')
