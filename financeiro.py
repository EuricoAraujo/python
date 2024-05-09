import requests
from requests.auth import HTTPBasicAuth
import os
import pandas as pd
from pandasai import Agent
from pandasai import SmartDataframe
from pandasai.connectors import MySQLConnector
from sqlalchemy import create_engine
from pandasai.llm import OpenAI
from pandasai.helpers.openai_info import get_openai_callback
from flask import Flask, request, jsonify

os.environ["PANDASAI_API_KEY"] = "$2a$10$RQ7877o4uyYYQZ.TGARcMOkJxdYVIms1qw4it9t90hmFYLCWR2FyG"

app = Flask(__name__)
@app.route('/api/requisicao', methods=['POST'])

def requisicao():
    # Obtemos os dados da requisição
    dados = request.json

    # Processamos os dados
    resultado = dados.get('valor')

    # Retornamos uma resposta
    return jsonify({'resultado': resultado})


def api():
    url = 'https://apiv2.sisloc.inf.br/api/parcelas/pagar/2024'
    basic = HTTPBasicAuth('api@adtrinformatica.com.br', '6330api@adtr')
    headers = {'Accept': 'application/json',"User-Agent": "XY"}
    response = requests.get(url,auth=basic,headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return response.headers

def main():
    repositorios = api()
    if repositorios:
        df = SmartDataframe(repositorios)
        while True:     
            message = input()
            response = df.chat(message)
            print(response)
    
    else:
        print(f'Não foi possível obter os repositórios de ')
        
        

if __name__ == '__main__':
    main()
    app.run(debug=True, port=8000)
