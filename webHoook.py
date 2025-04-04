from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.json
    print("Pagamento recebido:")
    print(dados)
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
