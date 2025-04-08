import threading
import requests
import time
import Variaveis


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST', 'HEAD'])
def ping():
    return jsonify({"status": "ativo | by Nox"}), 200

@app.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.json
    print("Pagamento recebido:")
    print(dados)

    # Grava status do pagamento
    with open("webhook_status.txt", "w") as f:
        f.write("CONFIRMADO")

    return '', 200

@app.route('/status', methods=['GET'])
def status_pagamento():
    try:
        with open("webhook_status.txt", "r") as f:
            status = f.read().strip()
        return jsonify({"pagamento": status}), 200
    except:
        return jsonify({"pagamento": "PENDENTE"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#Função Segundária Ant Queda
def mortovivo():
    while True:
        time.sleep(5)
        print("Executando no background...")
        resposta = requests.get(Variaveis.URL_STATUS, timeout=5)
        if resposta.status_code == 200:
            print("Serviço ativo")
        else:
            print("Serviço inativo")
        

# Inicia em segundo plano (daemon=True encerra com o programa principal)
threading.Thread(target=mortovivo, daemon=True).start()