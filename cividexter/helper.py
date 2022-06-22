from os import getenv
import requests
import json
from dotenv import load_dotenv

load_dotenv()


class Helper():
    def __init__(self) -> None:
        self.client = requests.session()


    def request_get(self):
        #TODO: LOGIN URL IN ENV
        url = 'https://cividex.herokuapp.com/api/token/'
        #TODO: USERNAME AND PASSWORD ENV
        login_data = {'username':'admin','password':'admin'}
        response = requests.post(url, login_data)
        response.status_code
        token = response.json()
        jwt = token['access']

        headers = {
        'Authorization': ('Bearer ' + jwt)
    }
        #TODO : Add django /api/ route to ENV
        fact_url = 'https://cividex.herokuapp.com/api/v1/facts/'
        response = requests.get(fact_url, headers=headers)
        #TODO: Return not print
        print(response.json())


helper = Helper()
helper.request_get()