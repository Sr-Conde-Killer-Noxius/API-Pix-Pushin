# =========================================
# 🚫 EVITA EXECUÇÃO DIRETA DO MÓDULO
# =========================================
if __name__ != "__main__":

    # =========================================
    # 📦 IMPORTAÇÃO DE MÓDULOS INTERNOS
    # =========================================
    import Conversor
    import captcharpixweboohk
    import Variaveis
    import Contrl_Erros
    import webHoook
    import User_Result_Line

    # =========================================
    # ⚙️ FUNÇÃO PRINCIPAL DE NIVELAMENTO
    # =========================================
    def Nivelamento_de_Solo():
        Variaveis.log.append("Executando Nivelador de Processos, Nivelamento de solo.")
        Conversor.pomba_correios()                        # Conversão de dados
        captcharpixweboohk.capthcar_pix_webhook()         # Captura webhook via CAPTCHA
        Contrl_Erros.deuruim()                            # Controle de exceções
        webHoook.run_mortovivo()                          # Inicia monitoramento background
        User_Result_Line.Result_line()                    # Retorna para User Result 
