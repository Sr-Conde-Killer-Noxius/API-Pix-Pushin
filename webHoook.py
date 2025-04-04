from flask import Flask, request, jsonify

app = Flask(__name__)

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
