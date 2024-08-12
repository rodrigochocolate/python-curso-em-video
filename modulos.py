from funcoes_ex107 import *

preco = float(input('Digite um preço: R$'))
print(f'A metade de R${preco:.2f} é igual a R${metade(preco):.2f}')
print(f'A dobro de R${preco:.2f} é igual a R${dobro(preco):.2f}')
print(f'Aumentando 10% de R${preco:.2f}, temos {aumentar(preco, 10):.2f}')