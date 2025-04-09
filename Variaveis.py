# ==========================
# 📦 IMPORTAÇÃO DE MÓDULOS
# ==========================
import User_Confi_varys  # Arquivo com variáveis externas configuráveis

# ==========================
# 💰 VARIÁVEIS FINANCEIRAS
# ==========================
Valor_Final_pix = 1100  # Valor do pagamento em centavos (ex: 1100 = R$11,00)
id_do_pix = 1  # Identificador único do pagamento

# ==========================
# 🌐 URLS EXTERNAS
# ==========================
URL_STATUS_CONFIG = User_Confi_varys.USER_URL_CONFIG  # Endpoint de status da API webhook

# ==========================
# 📡 STATUS / FEEDBACK
# ==========================
Status_QRCode = "Sem Dados a Mostrar"  # Status exibido quando não há QR gerado

# ==========================
# ⚙️ MENSAGENS DE INICIALIZAÇÃO
# ==========================
inciando_list = [
    "Iniciando",
    "Preparando ambiente",
    "Configurando ambiente",
    "Níveis Adicionados",
]

# ==========================
# ⏱️ CONTROLE DE EXECUÇÃO
# ==========================
Sleep_time = 1  # Delay entre execuções em segundos

# ==========================
# 🧾 LOGS DE EXECUÇÃO
# ==========================
log = []  # Log geral da execução
log_Erros = []  # Log de erros
Log_Contrl_Ant_queda = []  # Log do sistema de monitoramento anti-quedas

# ==========================
# 📂 ORGANIZAÇÃO VISUAL
# ==========================
log_org = "\n----------------------------------------\n"  # Separador visual no log

# ==========================
# 🛠️ CONTROLE DE EXECUÇÃO
# ==========================
RetornoHulk = 0  # Código genérico de retorno
ID_NivelamentoContrl = 0  # ID de controle para execução condicional
MAESTRO_DE_CERIMONIAS = "Runing_Apparence"
CORDENADOR_DE_CERIMONIAS = "Nivelador_de_Processos.py"
