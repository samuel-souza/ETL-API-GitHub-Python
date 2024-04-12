import getpass
from script import Extract, Transform, Load

# Meta, Apple, Netflix e Google
#  'Netflix', 'google'

companies = ['facebook', 'apple', 'Netflix', 'google']
token = getpass.getpass('Token: ')
dicionario = {
    'token': token,
    'username': 'samuel-souza',
    'name_repo': 'linguagens-utilizadas',
    'description': 'Adicionando dados'
}

for company in companies:
    lista = Extract(company, token).extract_data()
    Transform(lista).to_csv()

Load(dicionario, private = True).load_data()


