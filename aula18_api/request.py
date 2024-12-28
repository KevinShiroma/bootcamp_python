import requests

url = "https://servicodados.ibge.gov.br/api/v2/cnae/classes/"
response = requests.get(url)
response.encoding = 'utf-8'


data = response.json()
print(data)

id = data['id']
descricao = data['descricao']


print(id, descricao)