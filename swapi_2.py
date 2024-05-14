from typing import Type
from requests import Request
import requests

class HttpRequestError(Exception):
    def __init__(self, message, status_code) -> None:
        self.message = message
        self.status_code = status_code

class StarWarsApi:
    
    def star_wars_api(self, pesquisa: int):
        response = requests.Request(method='GET', url=f"https://swapi.dev/api/people/{pesquisa}/")
        req = response.prepare()
        response = self.__send_req(req)
        if response.status_code >= 200 and response.status_code <= 299:
            tupla = {'status_code': response.status_code, 'request': req, 'response': response.json()}
            print(tupla['status_code'])
            print(tupla['request'])
            print(tupla['response'])
            
        else:
            error = HttpRequestError(message = f"Erro: {response.json()['detail']}", status_code=response.status_code)
            print(error.message)
            print(error.status_code)
            print(Type[HttpRequestError])
        
        
    @classmethod
    def __send_req(self, req: Type[Request]) -> any:
        http_session = requests.Session()
        response = http_session.send(req)
        return response

def mae():
    pesquisa = int(input("Digite: "))
    resposta = StarWarsApi()
    resposta.star_wars_api(pesquisa)

mae()
