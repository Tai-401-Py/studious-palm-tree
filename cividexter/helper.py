#TODO: Uncomment after setting up .env
# from os import getenv
import random
import requests
from dotenv import load_dotenv

load_dotenv()


class Helper():
    def __init__(self) -> None:
        self.client = requests.session()
        self.filter = []


    def request_get(self):
        '''
        Retrieves information from back end
        '''
        #TODO: LOGIN URL IN ENV
        url = 'https://cividex.herokuapp.com/api/token/'
        #TODO: USERNAME AND PASSWORD ENV
        login_data = {'username':'admin','password':'admin'}
        response = requests.post(url, login_data)
        token = response.json()
        jwt = token['access']

        headers = {
        'Authorization': ('Bearer ' + jwt)
    }
        #TODO : Add django /api/ route to ENV
        fact_url = 'https://cividex.herokuapp.com/api/v1/facts/'
        response = requests.get(fact_url, headers=headers)
        #TODO: Return not print
        return self.request_parser(response.json())

    def request_parser(self, data):
        '''
        Parses the Get request from an array to a dictionary for easier searching
        '''
        for item in data:
            if item['verified'] is False:
                for key in item.keys():
                #TODO: Add query string and uncomment line below 
                    #if item[key] == query
                    self.filter.append(item)
        fact = random.sample(self.filter, 1)
        return fact[0]




helper = Helper()
helper.request_get()
