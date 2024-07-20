n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    print('-=-'*10)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair')
    print('-=-'*10)
    opcao = int(input('Qual sua opção? '))
    print('-=-'*10)
    if opcao == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor recebido foi {maior}')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        break
    else:
        print('Opção inválida. Tente novamente!')
print('-=-'*10)
print('Fim do programa. Volte sempre!')
