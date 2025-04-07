from flask import Flask, request, jsonify
import threading
import time
import random
import requests

app = Flask(__name__)

# === AUTO-PING ===
def auto_ping():
    while True:
        intervalo = random.randint(60, 150)  # entre 1min e 2min30s
        try:
            # render End Pint.
            requests.post("https://wehook-captcha.onrender.com/webhook", timeout=5)
            print("[Nox] Auto-ping enviado.")
        except Exception as e:
            print(f"[Nox] Erro no auto-ping: {e}")
        time.sleep(intervalo)

@app.route('/ping', methods=['POST'])
def ping():
    return "pong", 200

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
    # Inicia auto-ping em thread paralela
    threading.Thread(target=auto_ping, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
