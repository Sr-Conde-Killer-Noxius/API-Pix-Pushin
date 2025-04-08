import threading
import requests
import time
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Lista dinâmica de IDs válidos (em memória)
ids_validos = set()

# Substituindo o set simples por um dicionário
pagamentos = {}  # Ex: {"id_pix": "CONFIRMADO"}


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
def webhook():
    dados = request.get_json()
    id_pix = dados.get("id_pix")

    if not id_pix:
        return jsonify({"erro": "id_pix ausente"}), 400

    if id_pix in pagamentos:
        pagamentos[id_pix] = "CONFIRMADO"
        return jsonify({"status": "recebido"}), 200
    else:
        return jsonify({"erro": "id_pix não registrado"}), 404



@app.route('/status', methods=['GET'])
def status():
    id_pix = request.args.get("id_pix")

    if not id_pix:
        return jsonify({"erro": "id_pix não fornecido"}), 400

    status_pagamento = pagamentos.get(id_pix, "PENDENTE")
    return jsonify({
        "id_pix": id_pix,
        "pagamento": status_pagamento
    }), 200



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
