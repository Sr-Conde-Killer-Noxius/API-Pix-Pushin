import threading
import requests
import time
import Variaveis


from flask import Flask, request, jsonify
from flask import make_response

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST', 'HEAD'])
def ping():
    if request.method == 'HEAD':
        resposta = make_response('', 200)
        resposta.headers["X-Nox-Status"] = "ativo | by Nox"
        return resposta
    else:
        return jsonify({"status": "ativo | by Nox"}), 200
    

@app.route('/config', methods=['GET', 'POST', 'HEAD'])
def config():
    if request.method == 'HEAD':
        resposta = make_response('', 200)
        resposta.headers["X-Nox-Status-Config"] = "ativo | by Nox"
        return resposta
    else:
        return jsonify({"status-Config": "ativo | by Nox"}), 200


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

if __name__ != "__main__":# apenas para evitar execução direta
    import inspect
    import Variaveis
    import time
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
        origem = inspect.stack()[-1].filename.split("\\")[-1]
     
        ##print(f"[Nox] Chamador: {caller}")
        ##print(f"[Nox] Origem final: {origem}")     

        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 6: 

            return
        
        Variaveis.log.append("Iniciando monitoramento em segundo plano...")

        # Inicia em segundo plano (daemon=True encerra com o programa principal)
        threading.Thread(target=mortovivo, daemon=True).start()   
                