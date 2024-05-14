import requests

# people/1/ or planets/3/ or starships/9/

class StarWarsApi:
    @classmethod
    def star_wars_api(self, pesquisa: int):
        url = f"https://swapi.dev/api/people/{pesquisa}/"
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
        else:
            print("erro")

def mae():
    pesquisa = int(input("Digite: "))
    resposta = StarWarsApi()
    resposta.star_wars_api(pesquisa)

mae()
