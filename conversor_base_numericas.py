num = int(input('Digite um número inteiro: '))
print('Escolha uma das alternativas para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} converitdo para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} converitdo para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print(f'Opção inválida! Tente novamente.')
