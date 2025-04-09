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
    def Result_line():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]

        # 🛡️ Cadeado de segurança: trava tripla (origem + nivelamento + Start)
        if caller != Variaveis.CORDENADOR_DE_CERIMONIAS or Variaveis.ID_NivelamentoContrl != 76 or origem != Variaveis.MAESTRO_DE_CERIMONIAS:
            Variaveis.log_Erros.append("[Nox] Acesso indevido!.")
            Variaveis.log_Erros.append(f"[Nox] Chamador: {caller}")
            Variaveis.log_Erros.append(f"Nivel: {Variaveis.ID_NivelamentoContrl}")
            return

        print("Defina a ação a ser feita após o pagamento confirmado - line integration by Nox")