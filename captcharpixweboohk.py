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
        

        URL_STATUS = "https://api-pix-pushin.onrender.com/status"  # endpoint

        id_esperado = Variaveis.id_do_pix  # ID da cobrança esperada
        params = {"id_pix": id_esperado}
        tentativa = 0

        while True:
            try:
                resposta = requests.get(URL_STATUS, params=params, timeout=5)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    status = dados.get("pagamento", "")
                    id_recebido = dados.get("id_pix", "")

                    if id_recebido == id_esperado and status.lower() == "confirmado":
                        print("✅ Pagamento confirmado!")
                        break

                tentativa += 1
                print(f"⏳ Aguardando confirmação de pagamento via webhook... ({tentativa})", end='\r')

                if tentativa >= 60:
                    print("❌ Tempo limite excedido. Pagamento não confirmado.")
                    break

                time.sleep(5)

            except Exception as e:
                print(f"Erro na verificação de status: {e}")
                time.sleep(5)
