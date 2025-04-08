# captcharpixweboohk.py
if __name__ != "__main__":# modulo_nox.py
    import inspect
    import Variaveis


    def capthcar_pix_webhook():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]
        
        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 1:

            Variaveis.log_Erros.append("[Nox] Acesso indevido à função capthcar_pix_webhook.")
            Variaveis.log_Erros.append(f"[Nox] Chamador: {caller}")
            Variaveis.log_Erros.append(f"Nível : {Variaveis.ID_NivelamentoContrl}")

            return
        
        import requests
        import time

        URL_STATUS = "https://api-pix-pushin.onrender.com/status"  # endpoint que o Render expõe

        print("⏳ Aguardando confirmação de pagamento via webhook...")

        id_esperado = Variaveis.id_do_pix  # ID atual da cobrança

        while True:
            try:
                resposta = requests.get(URL_STATUS, timeout=5)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    status = dados.get("pagamento", "")
                    id_recebido = dados.get("id_pix", "")

                    if status == "CONFIRMADO" and id_recebido == id_esperado:
                        print("✅ Pagamento confirmado com sucesso!")
                        break
                    else:
                        print("🔄 Aguardando... Status:", status, "| ID:", id_recebido)
                else:
                    print(f"⚠️ Erro na requisição: {resposta.status_code}")
            except Exception as erro:
                print(f"❌ Erro ao consultar status: {erro}")

            time.sleep(3)
