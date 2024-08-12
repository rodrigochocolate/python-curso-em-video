from funcoes_moeda import *

preco = float(input('Digite um preço: R$'))
print(f'A metade de {formatarDinheiro(preco, 'r$')} é igual a {formatarDinheiro(metade(preco), 'r$')}')
print(f'A dobro de {formatarDinheiro(preco, 'r$')} é igual a {formatarDinheiro(dobro(preco), 'r$')}')
print(f'Aumentando 10% de R${formatarDinheiro(preco, 'r$')}, temos {formatarDinheiro(aumentar(preco, 10))}')