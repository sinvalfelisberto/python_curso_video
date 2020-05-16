import json
import requests

requisition = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/')
print(requisition.text)
