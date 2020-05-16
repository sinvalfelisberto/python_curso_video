import requests
import json
import datetime
import time


while True:
    req = requests.get('https://economia.awesomeapi.com.br/json/all')
    
    date_now = datetime.datetime.now()
    date_now_str = date_now.strftime('%d/%m/%Y %H:%M')
    quotetion = json.loads(req.text)
    dolar = float(quotetion['USD']['high'])
    euro = float(quotetion['EUR']['high'])
    bitcoin = float(quotetion['BTC']['high'])
    print(date_now_str)
    print(f'Dollar: R$  {dolar}')
    print(f'Euro: R$  {euro}')
    print(f'BitCoin: R$ {bitcoin}')
    print('--' * 20)
    time.sleep(30)
