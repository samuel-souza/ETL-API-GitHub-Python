import pandas as pd
import os

class Transform():

    def __init__(self, list_repo: list) -> None:
        self.__list = list_repo

    def __get_owner(self) -> str:
        owner_repo = self.__list[0][0]['full_name'].split('/')[0]
        return owner_repo
    
    def __get_names(self) -> list:
        name_list = []

        for page in self.__list:
            for repo in page:
                name_list.append(repo['name'])
        
        return name_list
    
    def __get_languages(self) -> list:
        languages_list = []

        for page in self.__list:
            for repo in page:
                languages_list.append(repo['language'])
        
        return languages_list
        
    def to_csv(self) -> None:

        data = {
            'repositories_names': self.__get_names(),
            'repositories_languages': self.__get_languages()
        }

        df = pd.DataFrame(data)

        owner = self.__get_owner()

        folder = './data'

        if not os.path.exists(folder):
            os.makedirs(folder)

        df.to_csv(f'{folder}/{owner}_languages.csv',index=False)




        


    