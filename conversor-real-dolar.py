import json
import requests

url = 'https://economia.awesomeapi.com.br/json/last/'+ 'USD' +'-'+ 'BRL'
cotacao = round(float(json.loads(requests.get(url).content)['USDBRL']['bid']), 2)
real = float(input('Quanto você tem na carteira? '))
dolar = real / cotacao

print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
