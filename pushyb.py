#Importando Librearias
import requests
import inspect
import Runing_Apparence

#Importando Arquivos Py
import Variaveis

def Captar_Valor_Final(Valor_Final_pix):

    Valor_Final_pix = input("Digite o Valor do Pix: ")

    return Valor_Final_pix



# URL da API de cobrança
URL_COBRANCA = "https://api.pushinpay.com.br/api/pix/cashIn"

# Seu token de autenticação
TOKEN = "22756|bDLE9HZPWtmH29MbGuNejjgRl0WroCe034kg2Qtw476707f4"

# Criando o dicionário de dados com a função integrada
dados = {
    "value": Variaveis.Valor_Final_pix,  # Valor em centavos (ex: R$10.00 -> 1000)
    "webhook_url": "https://api-pix-pushin.onrender.com/webhook",
    "id_pix": Variaveis.id_do_pix,
}


# Cabeçalhos da requisição
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}


if __name__ == "__main__":
    # Executa a função abaixo quando o script é executado diretamente
    print("Sem Função")