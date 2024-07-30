from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def consultar_cepito(cep):
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
#http://localhost:5000/consultar-cep?cep=69005100
@app.route("/consultar-cep", methods=['GET'])
def consultar_cepito_endpoint():
    cep = request.args.get('cep')
    if cep:
        resultado = consultar_cepito(cep)
        if resultado:
            return jsonify(resultado)
        else:
            return jsonify({"erro": "CEP não encontrado"})
    else:
        return jsonify({"erro": "CEP não informado"}), 400

def mae():
    app.run(debug=True)

mae()