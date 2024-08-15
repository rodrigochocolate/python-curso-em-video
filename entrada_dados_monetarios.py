from ex111.utilidades import moeda, dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 50, 20)