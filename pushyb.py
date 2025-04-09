# =========================================
# 📦 IMPORTAÇÃO DE BIBLIOTECAS
# =========================================
import requests           # Requisições HTTP (API)
import inspect            # Análise do contexto de execução
import Runing_Apparence   # Aparência visual customizada

# =========================================
# 🔗 IMPORTAÇÃO DE MÓDULOS INTERNOS
# =========================================
import Variaveis
import User_Confi_varys   # Configurações sensíveis e personalizáveis

# =========================================
# 🧮 FUNÇÃO PARA CAPTURA DO VALOR VIA INPUT
# =========================================
def Captar_Valor_Final(Valor_Final_pix):
    Valor_Final_pix = input("Digite o Valor do Pix: ")
    return Valor_Final_pix

# =========================================
# 🌐 DADOS DE CONFIGURAÇÃO PARA ENVIO DO PIX
# =========================================

# Endpoint de cobrança da API PushinPay
URL_COBRANCA = User_Confi_varys.USER_URL_COBRANCA

# Token de autenticação do usuário
TOKEN = User_Confi_varys.USER_TOKEN

# Corpo (payload) da requisição de cobrança
dados = {
    "value": Variaveis.Valor_Final_pix,                 # Valor em centavos (ex: R$ 10,00 → 1000)
    "webhook_url": User_Confi_varys.USER_WEB_HOOK_URL,  # URL que receberá notificações
    "id_pix": Variaveis.id_do_pix                       # ID único da transação
}

# Headers da requisição HTTP
headers = {
    "Authorization": f"Bearer {TOKEN}",                  # Autenticação via Bearer Token
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# =========================================
# ⚙️ EXECUÇÃO DIRETA DO SCRIPT
# =========================================
if __name__ == "__main__":
    print("Sem Função")  # Placeholder para execução direta
