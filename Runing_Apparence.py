# =============================================
# 🔗 IMPORTAÇÃO DE ARQUIVOS INTERNOS (.py)
# =============================================
import Variaveis           # Variáveis globais e de controle
import pushyb              # Módulo para captura de valor
import Conversor           # Conversor de formatos de valor

# =============================================
# 🧩 IMPORTAÇÃO DE BIBLIOTECAS EXTERNAS
# =============================================
import time                # Controle de tempo (delays)

# =============================================
# 💰 CAPTURA INICIAL DO VALOR
# =============================================
Captar_Valor_Final = Variaveis.Valor_Final_pix

# =============================================
# ▶️ EXECUÇÃO PRINCIPAL - MAESTRO DOS NÍVEIS
# =============================================
if __name__ == "__main__":
    import Nivelador_de_Processos  # Import dinâmico apenas se for execução direta

    # 🟢 Inicialização visual do ambiente
    for ignicao in Variaveis.inciando_list:
        print(ignicao)
        time.sleep(Variaveis.Sleep_time)  # Delay de inicialização

    # 🛡️ Ativando sistema anti-quedas
    Variaveis.ID_NivelamentoContrl = 6
    Nivelador_de_Processos.Nivelamento_de_Solo()

    # 💸 Captura e conversão do valor final do pagamento
    Captar_Valor_Final = pushyb.Captar_Valor_Final(Captar_Valor_Final)
    Captar_Valor_Final = Conversor.tratar_valor_fina_input(Captar_Valor_Final)
    Variaveis.log.append(
        f"Valor Final: R$ {Captar_Valor_Final / 100:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    # 🔁 Atualização do valor na memória
    Variaveis.Valor_Final_pix = Captar_Valor_Final

    # 🔄 Executando novamente nivelador de processos
    Variaveis.ID_NivelamentoContrl = 2
    Nivelador_de_Processos.Nivelamento_de_Solo()

    # 🖨️ Imprimindo todos os logs capturados
    for log_atual in Variaveis.log:
        print(log_atual)
        time.sleep(Variaveis.Sleep_time)

    print(Variaveis.log_org)
    print(Variaveis.Status_QRCode)
    print(Variaveis.log_org)

    # =========================
    # 🔚 FINALIZAÇÃO DO PROCESSO
    # =========================
    def finish():
        Variaveis.ID_NivelamentoContrl = 1    
        Nivelador_de_Processos.Nivelamento_de_Solo()

    finish()
    print("Finalizando...")
    Nivelador_de_Processos.Nivelamento_de_Solo()
    Variaveis.ID_NivelamentoContrl = 545

    # 🔄 Atualização final do valor
    Variaveis.Valor_Final_pix = Captar_Valor_Final
