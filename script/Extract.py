import requests

class Extract:

    def __init__(self, owner: str, token: str) -> None:
        self.__owner = owner
        self.__api_url = 'https://api.github.com'
        self.__token = token
        self.__headers = {'Authorization': 'Bearer ' + self.__token, 'X-GitHub-Api-Version': '2022-11-28'}

    
    def __num_pages(self) -> int:
        url = f'{self.__api_url}/users/{self.__owner}/repos'
        response = requests.get(url, headers = self.__headers)

        link_response = response.headers.get('Link')

        if link_response:
            num_pages = int(link_response.split(',')[-1].split(';')[0].split('page=')[-1].split('>')[0])
        
        return num_pages


    def extract_data(self) -> list:
        list_repo = []
        num = self.__num_pages() 

        for n in range(1, num):
            try: 
                url_endpoint = f'{self.__api_url}/users/{self.__owner}/repos?page={n}'
                response = requests.get(url_endpoint, headers = self.__headers)
                list_repo.append(response.json())
            except:
                list_repo.append(None)
        
        return list_repo


    

        


        
    




