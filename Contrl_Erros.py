# =========================================
# 🚫 EVITA EXECUÇÃO DIRETA DO MÓDULO
# =========================================
import Variaveis

if __name__ != "__main__":

    # =========================================
    # 📦 IMPORTAÇÃO DE MÓDULOS INTERNOS/EXTERNOS
    # =========================================
    import inspect
    import Variaveis
    import time

    # =========================================
    # 🛠️ FUNÇÃO DE EXIBIÇÃO DE LOGS DE ERRO
    # =========================================
    def deuruim():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]

        # 🛡️ Cadeado de segurança: trava dupla (origem + nivelamento)
        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 3:
            return

        print("Iniciando Relatório de Erros:")
        for Log_Erro_atual in Variaveis.log_Erros:
            print(Log_Erro_atual)
            time.sleep(Variaveis.Sleep_time)  # Atraso configurado em Variaveis
