# 💸 Noxius PushinPay API

> API em Flask para controle de cobranças via PIX com verificação automática por webhook.  
> Desenvolvido por **Sr. Nox** | Rei da Capital Digital™

---

## ⚙️ Funcionalidades

✅ Registro de cobranças via `id_pix`  
✅ Webhook para confirmação automática de pagamento  
✅ Consulta pública do status de cada ID  
✅ Endpoints `ping` e `config` para monitoramento  
✅ Monitoramento silencioso em segundo plano (background)

---

## 🔗 Endpoints

### 🔍 `GET /ping`
Retorna o status da API.  
**Resposta:**  
```json
{ "status": "ativo | by Nox" }
```

---

### ⚙️ `GET /config`
Verifica se a API está operando com configuração ativa.  
**Resposta:**  
```json
{ "status-Config": "ativo | by Nox" }
```

---

### 📝 `POST /registrar-id`
Registra um novo ID de cobrança.

**Body JSON:**
```json
{ "id": "exemplo-id-pix" }
```

**Resposta:**  
```json
{ "status": "ID registrado com sucesso" }
```

---

### ✅ `GET /verificar-id?id=EXEMPLO`
Verifica se o ID foi previamente registrado.

**Resposta (200):**
```json
{ "valido": true }
```

**Resposta (404):**
```json
{ "valido": false }
```

---

### 📩 `POST /webhook`
Confirma o pagamento de um ID via sistema externo (PushinPay).

**Body JSON:**
```json
{ "id": "exemplo-id-pix" }
```

**Resposta:**  
```json
{ "status": "recebido" }
```

---

### 📊 `GET /status?id=EXEMPLO`
Consulta o status atual de pagamento de um ID.

**Resposta:**
```json
{
  "id": "exemplo-id-pix",
  "pagamento": "CONFIRMADO" // ou "PENDENTE"
}
```

---

## 🧠 Lógica do Sistema

- Todos os `id_pix` devem ser registrados antes da confirmação.
- O Webhook só confirma IDs válidos.
- O status é salvo na memória (`pagamentos[id] = status`).
- Opcional: um monitoramento em background pode ser ativado ao importar o módulo corretamente.

---

### 🌐 Webhook Externo com Render

Para utilizar o **webhook real da PushinPay**, é necessário publicar o arquivo `webhook.py` no [Render](https://render.com/):

- Crie um novo projeto no Render
- Faça deploy do `webhook.py` como serviço web
- O Render gerará uma URL como:
  
```
https://webhook-noxius.onrender.com/webhook
```

Essa URL será usada como destino do webhook de confirmação de pagamento.

---

### 🔒 Sistema Anti-Queda Imbutido

A API possui um sistema **anti-quedas** embutido que:

- Executa em segundo plano automaticamente (`background`)
- Monitora se a API está online em ciclos aleatórios entre **9 a 14 minutos**
- Loga status internamente usando a variável `Log_Contrl_Ant_queda`
- É ativado apenas em ambiente importado com verificação condicional, evitando sobrecarga fora de produção

Isso garante que o **serviço continue operando no Render**, mesmo com possíveis inatividades temporárias.

---

## 🚀 Executando a API

```bash
Runing_Apparence
```

A API será iniciada em:

```
http://0.0.0.0:5000
```

---

## 🧪 Testes Rápidos via `curl`

```bash
curl http://localhost:5000/ping

curl -X POST http://localhost:5000/registrar-id \
  -H "Content-Type: application/json" \
  -d '{"id":"abc-123"}'

curl http://localhost:5000/status?id=abc-123
```

---

## 📦 Requisitos

- Python 3.8+
- Flask
- Requests

---

## 📄 Arquivo `requirements.txt`

```
Flask==2.3.2
requests==2.31.0
```

---

## 👑 Autor

Desenvolvido por **Sr. Nox**  
Diretor da **Capital Digital™**

---
