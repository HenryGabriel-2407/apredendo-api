import requests
import json

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return data
        else:
            return None 
    else:
        print("Erro ao consultar el cepito")
        return None
    
def mae():
    continuar = True
    while continuar:
        cep = input("\nDigite o CEP que deseja consultar ou digite 'sair': ")
        if cep.lower() == 'sair':
            print("Tchau otário!")
            break
        resultado = consultar_cep(cep)
        if resultado:
            print("CEP encontrado")
            print(f"CEP: {resultado['cep']}")
            print(f"Logradouro: {resultado['logradouro']}")
            print(f"Complemento: {resultado['complemento']}")
            print(f"Bairro: {resultado['bairro']}")
            print(f"Cidade: {resultado['localidade']}")
            print(f"Estado: {resultado['uf']}")
            print("UFA!")
        else:
            print("Cadê o CEP???")
        print()

mae()