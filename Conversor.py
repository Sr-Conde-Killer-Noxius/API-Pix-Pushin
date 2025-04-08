
import Variaveis


if __name__ != "__main__":# apenas para evitar execução direta
    import inspect
    import Variaveis
    import pushyb
    import json
    import uuid


    def tratar_valor_fina_input(valor):
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]

        ##print(f"[Nox] Chamador: {caller}")
        ##print(f"[Nox] Origem final: {origem}")

        
        
        if caller != "Runing_Apparence.py":
            
            Variaveis.log_Erros.append("[Nox] Acesso indevido a dado de Valores!.")
            Variaveis.log_Erros.append(f"[Nox] Chamador: {caller}")
            Variaveis.log_Erros.append(f"Nivel: {Variaveis.ID_NivelamentoContrl}")
            
            return 
        
        valor = valor.replace(".", "").replace(",", ".")
        try:
            valor_float = float(valor)
            return int(valor_float * 100)
        except ValueError:
            print("Erro: Número inválido.")
            return tratar_valor_fina_input(input("Digite novamente: "))

            


    def pomba_correios():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]

        ##print(f"[Nox] Chamador: {caller}")
        ##print(f"[Nox] Origem final: {origem}")
        

        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 2:  

            Variaveis.log_Erros.append("[Nox] Acesso indevido à função pomba_correios - NLV!.")  
            Variaveis.log_Erros.append(f"[Nox] Chamador: {caller}")
            Variaveis.log_Erros.append(f"Nivel: {Variaveis.ID_NivelamentoContrl}")

            return        
        
        Variaveis.log.append("Executando Verificações de Inicialização")
        Variaveis.log.append("Nivelador de Processos Iniciado com Sucesso Pomba Correios")
        Variaveis.id_do_pix = str(uuid.uuid4())
        print(f"Id do pix: {Variaveis.id_do_pix}")
        pushyb.dados["id_pix"] = Variaveis.id_do_pix
        pushyb.dados["value"] = Variaveis.Valor_Final_pix
        Variaveis.log.append("Enviando dados para cobrança PIX...")
        # Registrar o ID no servidor
        pushyb.requests.post("https://api-pix-pushin.onrender.com/registrar-id", json={
        "id":Variaveis.id_do_pix
        })

        try:
            resposta = pushyb.requests.post(pushyb.URL_COBRANCA, json=pushyb.dados, headers=pushyb.headers)
            dados_resposta = resposta.json()

            if "qr_code" in dados_resposta:
                Variaveis.Status_QRCode = dados_resposta["qr_code"]

            else:
                Variaveis.Status_QRCode = "Erro: Código PIX ausente na resposta."

            with open("log_pix.json", "w", encoding="utf-8") as log_file:
                json.dump(dados_resposta, log_file, indent=4, ensure_ascii=False)

        except Exception as e:
            Variaveis.log.append(f"Erro durante o envio: {e}")
            Variaveis.Status_QRCode = "Erro de comunicação."
        else:
            Variaveis.log_Erros.append("[Nox] Acesso indevido à função pomba_correios - Nível -1.")