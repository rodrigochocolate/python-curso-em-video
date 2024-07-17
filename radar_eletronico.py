velocidade = int(input('Velocidade do carro (Km/h)? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você excedeu a velocidade limite de 80Km/h, você está multado em R${multa:.2f}!')
    
print('Tenha um ótimo dia, dirija com segurança!')
