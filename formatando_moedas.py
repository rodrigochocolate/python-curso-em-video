from funcoes_moeda import *

preco = float(input('Digite um preço: R$'))
print(f'A metade de {formatarDinheiro(preco, 'r$')} é igual a {metade(preco, True)}')
print(f'A dobro de {formatarDinheiro(preco, 'r$')} é igual a {dobro(preco, True)}')
print(f'Aumentando 10% de R${formatarDinheiro(preco, 'r$')}, temos {aumentar(preco, 10, True)}')