def voto(ano_de_nascimento):
    from datetime import datetime
    
    ano_atual = datetime.today().year
    idade = ano_atual - ano_de_nascimento
    
    if idade < 16:
        return 'NEGADO'
    elif idade < 18:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'
    
num = int(input('Ano de nascimento: '))
print(f'Seu voto é {voto(num)}!')