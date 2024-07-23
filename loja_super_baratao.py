# CABEÇALHO
print('-' * 30)
print('LOJA SUPER BARATÃO'.center(30))
print('-' * 30)

totalDaCompra = produtoCaro = 0
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))   
    
    # NÃO VALIDANDO PREÇOS NEGATIVOS
    while preco < 0:
        print('Digite um preço válido!')
        preco = float(input('Preço: R$'))
    
    #PREÇO TOTAL DAS COMPRAS
    totalDaCompra += preco
    
    # PRODUTO MAIS BARATO
    if totalDaCompra == preco or preco < precoMaisBarato:
        precoMaisBarato = preco
        maisBarato = produto
    
    # PRODUTOS MAIS QUE R$1000,00
    if preco > 1000:
        produtoCaro += 1
        
    # CONTINUAR OU NÃO
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(' FIM DO PROGRAMA '.center(30, '-'))
print('O total da compra foi R${:.2f}'.format(totalDaCompra))
print('Temos {} produto(s) custando mais de R$1000.00'.format(produtoCaro))
print('O produto mais barato foi {} que custa R${:.2f}'.format(maisBarato, precoMaisBarato))
