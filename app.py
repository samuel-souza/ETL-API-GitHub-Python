import getpass
from script import Extract, Transform, Load

companies = ['facebook', 'apple', 'Netflix', 'google']
token = getpass.getpass('Token: ')
params = {
    'token': token,
    'username': 'samuel-souza',
    'name_repo': 'linguagens-utilizadas',
    'description': 'Adicionando dados'
}

for company in companies:
    lista = Extract(company, token).extract_data()
    Transform(lista).to_csv()

Load(params, private = True).load_data()


