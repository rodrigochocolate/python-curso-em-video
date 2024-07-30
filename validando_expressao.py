expre = str(input('Digite a expressao: '))
cont = 0
for x in expre:
    if x == '(':
        cont += 1
    elif x == ')':
        cont -= 1
        if cont < 0: ## Fechou antes de abrir
            print('Expressao invalida')
            exit(0) # Termina programa

if cont != 0: ## Tem parenteses sem seu par
    print('Expressao invalida')
else:
    print('Expressao valida')