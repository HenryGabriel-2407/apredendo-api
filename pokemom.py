import requests
import json

def cacar_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if 'erro' not in dados:
            return dados
        else:
            return None
    else:
        print(f"Erro ao pesquisar o pokémon: {response.status_code}")
        return None

def mae():
    while True:
        pokemon = input("Digite o pokemon que quer caçar ou 'sair': ")
        if pokemon.lower() == 'sair':
            print("Tchau! Tchau!")
            break
        resultado = cacar_pokemon(pokemon.lower())
        if resultado:
            print(f"\tNome: {resultado['name']}")
            print(f"\tTipo: {resultado['types'][0]['type']['name']}")
        print()
    pass

mae()