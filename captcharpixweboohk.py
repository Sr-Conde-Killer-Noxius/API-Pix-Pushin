# captcharpixweboohk.py
if __name__ != "__main__":# modulo_nox.py
    import inspect
    import Variaveis


    # Adiciona log de execução
    Variaveis.log.append("Executando Verificações de Inicialização")


    def capthcar_pix_webhook():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]
        
        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 1:

            print("[Nox] Acesso indevido à função capthcar_pix_webhook.")
            print(f"[Nox] Chamador: {caller}")
            print(f"Nível : {Variaveis.ID_NivelamentoContrl}")

            return
        
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
