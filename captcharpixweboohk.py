# captcharpixweboohk.py
import requests
import time

URL_STATUS = "https://api-pix-pushin.onrender.com/status"  # endpoint que o Render expõe

print("⏳ Aguardando confirmação de pagamento via webhook...")

while True:
    try:
        resposta = requests.get(URL_STATUS, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            status = dados.get("pagamento", "")
            if status == "CONFIRMADO":
                print("✅ Pagamento confirmado com sucesso!")
                break
            else:
                print("🔄 Pagamento ainda não confirmado...")
        else:
            print(f"⚠️ Erro na requisição: {resposta.status_code}")
    except Exception as erro:
        print(f"❌ Erro ao consultar status: {erro}")
    
    time.sleep(3)  # espera 3 segundos antes de tentar novamente
