# =========================================
# 📄 captcharpixweboohk.py
# =========================================

# 🚫 Evita execução direta do módulo
if __name__ != "__main__":

    # 📦 Importações
    import inspect
    import Variaveis

    # =========================================
    # 🔐 Validador de Pagamento via Webhook (PIX)
    # =========================================
    def capthcar_pix_webhook():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]

        # 🛡️ Cadeado de segurança: trava dupla (origem + nivelamento)
        if caller != Variaveis.CORDENADOR_DE_CERIMONIAS or Variaveis.ID_NivelamentoContrl != 1:
            Variaveis.log_Erros.append("[Nox] Acesso indevido à função capthcar_pix_webhook.")
            Variaveis.log_Erros.append(f"[Nox] Chamador: {caller}")
            Variaveis.log_Erros.append(f"Nível : {Variaveis.ID_NivelamentoContrl}")
            return

        # 📦 Importações locais
        import requests
        import time
        import json 
        import User_Confi_varys


        URL_STATUS = User_Confi_varys.USER_URL_STATUS  # Endpoint de status

        with open("log_pix.json", "r", encoding="utf-8") as file:
            dados = json.load(file)
            Variaveis.id_do_pix = dados.get("id", "")

        id_esperado = Variaveis.id_do_pix
        params = {"id": id_esperado}
        tentativa = 0

        # 🔁 Loop de verificação contínua
        while True:
            try:
                resposta = requests.get(URL_STATUS, params=params, timeout=5)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    status = dados.get("pagamento", "")
                    id_recebido = dados.get("id", "")

                    if id_recebido == id_esperado and status.lower() == "confirmado":
                        print("✅ Pagamento confirmado!")
                        Variaveis.ID_NivelamentoContrl = 76
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
