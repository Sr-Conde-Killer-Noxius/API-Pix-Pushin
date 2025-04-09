# ==========================
# 🔧 CONFIGURAÇÕES GERAIS
# ==========================

# URL para criar cobranças (PushinPay)
USER_URL_COBRANCA = "https://api.pushinpay.com.br/api/pix/cashIn"

# Token de autenticação do usuário
USER_TOKEN = "22756|bDLE9HZPWtmH29MbGuNejjgRl0WroCe034kg2Qtw476707f4"

# URL base do Webhook (Render, etc.)
USER_WEB_HOOK_BASE = "https://api-pix-pushin.onrender.com"

# ==========================
# 🔁 ENDPOINTS DINÂMICOS
# ==========================

USER_WEB_HOOK_URL = f"{USER_WEB_HOOK_BASE}/webhook"
USER_URL_PING = f"{USER_WEB_HOOK_BASE}/ping"
USER_URL_CONFIG = f"{USER_WEB_HOOK_BASE}/config"
USER_URL_REGISTRAR_ID = f"{USER_WEB_HOOK_BASE}/registrar-id"
USER_URL_VERIFICAR_ID = f"{USER_WEB_HOOK_BASE}/verificar-id"
USER_URL_STATUS = f"{USER_WEB_HOOK_BASE}/status"
