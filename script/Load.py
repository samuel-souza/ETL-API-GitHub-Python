import requests
import base64
import os

class Load:

    def __init__(self, params: dict, private: bool = False) -> None:
        self.__token = params['token']
        self.__username = params['username']
        self.__name_repo = params['name_repo']
        self.__description = params['description']
        self.__private = private

        
        self.__path = './data'
        self.__headers = {'Authorization': 'Bearer ' + self.__token, 'X-GitHub-Api-Version': '2022-11-28'}
        self.__api_url_post = 'https://api.github.com/user/repos'
        self.__api_url_put = f'https://api.github.com/repos/{self.__username}/{self.__name_repo}/contents/data/'


    def __create_repo(self) -> None:

        data_create = {
            'name': self.__name_repo,
            'description': self.__description,
            'private': self.__private
        }

        print('Criando repositório...')
        response = requests.post(self.__api_url_post, json = data_create, headers = self.__headers)
        print(response.status_code)

    def __encoding_data(self) -> list:

        list_file_content = []
        list_file_name = []

        for filename in os.listdir(self.__path):
            if filename.endswith('.csv'):
                filepath = os.path.join(self.__path, filename)
            
            with open(filepath, 'rb') as file:
                file_content = file.read()
    
            list_file_content.append(base64.b64encode(file_content))
            list_file_name.append(filename.split('.')[0])

        return (list_file_name, list_file_content)

    def load_data(self) -> None:
        
        self.__create_repo()

        name, encoded_contents = self.__encoding_data()

        print('Adicionando dados ao repositório...')

        for name, content in zip(name, encoded_contents):
            data_content = {
                'message': 'Adicionando arquivo referente as linguagens utilizadas',
                'content': content.decode('utf-8')
            }
        
            response = requests.put(f'{self.__api_url_put}{name}.csv', json = data_content, headers = self.__headers)
            print(response.status_code)

