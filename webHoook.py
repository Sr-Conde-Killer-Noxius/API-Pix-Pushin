import threading
import requests
import time
import os
import json
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Lista dinâmica de IDs válidos (em memória)
ids_validos = set()

@app.route('/ping', methods=['GET', 'POST', 'HEAD'])
def ping():
    if request.method == 'HEAD':
        resposta = make_response('', 200)
        resposta.headers["X-Nox-Status"] = "ativo | by Nox"
        return resposta
    return jsonify({"status": "ativo | by Nox"}), 200

@app.route('/config', methods=['GET', 'POST', 'HEAD'])
def config():
    if request.method == 'HEAD':
        resposta = make_response('', 200)
        resposta.headers["X-Nox-Status-Config"] = "ativo | by Nox"
        return resposta
    return jsonify({"status-Config": "ativo | by Nox"}), 200

@app.route('/registrar-id', methods=['POST'])
def registrar_id():
    dados = request.json
    id_pix = dados.get("id")
    if not id_pix:
        return jsonify({"erro": "ID não informado"}), 400
    ids_validos.add(id_pix)
    return jsonify({"status": "ID registrado com sucesso"}), 200

@app.route('/verificar-id', methods=['GET'])
def verificar_id():
    id_pix = request.args.get("id")
    if id_pix in ids_validos:
        return jsonify({"valido": True}), 200
    return jsonify({"valido": False}), 404

@app.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.json
    id_recebido = dados.get("id_pix")
    print("Pagamento recebido:")
    print(dados)

    # Verifica se o ID é válido
    if id_recebido not in ids_validos:
        print(f"❌ ID PIX inválido: {id_recebido}")
        return '', 403

    print("✅ Pagamento confirmado:")
    print(dados)

    # Grava status do pagamento
    with open("webhook_status.txt", "w") as f:
        f.write("CONFIRMADO")

    # Remove ID validado (opcional)
    ids_validos.discard(id_recebido)

    return '', 200

@app.route('/status', methods=['GET'])
def status_pagamento():
    try:
        with open("webhook_status.txt", "r") as f:
            status = f.read().strip()
        return jsonify({"pagamento": status}), 200
    except:
        return jsonify({"pagamento": "PENDENTE"}), 200

# Execução principal
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

# Background monitoramento (somente se importado corretamente)
if __name__ != "__main__":
    import inspect
    import Variaveis
    import random

    def mortovivo():
        while True:
            time.sleep(random.randint(540, 840))
            Variaveis.Log_Contrl_Ant_queda.append("Executando no background...")
            resposta = requests.get(Variaveis.URL_STATUS_CONFIG, timeout=random.randint(5, 10))
            if resposta.status_code == 200:
                Variaveis.Log_Contrl_Ant_queda.append("Serviço ativo")
            else:
                Variaveis.Log_Contrl_Ant_queda.append("Serviço inativo")

    def run_mortovivo():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 6:
            return
        Variaveis.log.append("Iniciando monitoramento em segundo plano...")
        threading.Thread(target=mortovivo, daemon=True).start()
