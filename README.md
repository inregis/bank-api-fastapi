# 🏦 Bank API FastAPI

API bancária assíncrona desenvolvida com **FastAPI**, aplicando autenticação JWT, regras de negócio financeiras e arquitetura em camadas.

---

## 🚀 Funcionalidades

- Cadastro de usuários
- Login com autenticação JWT
- Proteção de rotas
- Criação de contas bancárias
- Depósito
- Saque
- Extrato completo
- Validação de regras de negócio
- Tratamento de exceções

---

## 🛠 Tecnologias utilizadas

- Python 3.14
- FastAPI
- SQLAlchemy Async
- SQLite
- JWT Authentication
- Poetry
- Uvicorn

---

## 📂 Estrutura do projeto

```bash
src/
├── controllers/
├── models/
├── schemas/
├── services/
├── config.py
├── database.py
├── exceptions.py
├── main.py
└── security.py
```

---

## 🧱 Arquitetura

O projeto foi estruturado seguindo separação por responsabilidades:

### Controllers
Responsáveis pelos endpoints da API.

### Services
Implementação das regras de negócio.

### Models
Mapeamento das entidades no banco.

### Schemas
Validação e serialização de dados.

### Security
Autenticação JWT e proteção de rotas.

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/inregis/bank-api-fastapi.git
```

Entre na pasta:

```bash
cd bank-api-fastapi
```

Instale as dependências:

```bash
poetry install
```

Execute o projeto:

```bash
poetry run uvicorn src.main:app --reload
```

---

## 📖 Documentação Swagger

Acesse:

```text
http://127.0.0.1:8000/docs
```

---

## 🔐 Fluxo de autenticação

### 1. Criar usuário

`POST /auth/register`

---

### 2. Fazer login

`POST /auth/login`

Retorna:

```json
{
  "access_token": "token",
  "token_type": "bearer"
}
```

---

### 3. Autorizar no Swagger

Clique em **Authorize**

Insira:

```text
Bearer SEU_TOKEN
```

---

## 💰 Endpoints bancários

### Criar conta
`POST /accounts`

### Consultar conta
`GET /accounts/{id}`

### Depositar
`POST /transactions/{id}/deposit`

### Sacar
`POST /transactions/{id}/withdraw`

### Extrato
`GET /transactions/{id}/statement`

---

## ✅ Regras de negócio implementadas

- Não permite depósito negativo
- Não permite saque negativo
- Não permite saque sem saldo
- Rotas protegidas por autenticação
- Extrato completo com histórico

---

## 🧪 Testes realizados

- Cadastro de usuário
- Login
- Autorização JWT
- Depósito válido/inválido
- Saque válido/inválido
- Extrato
- Proteção de endpoints

---

## 📌 Objetivo

Projeto desenvolvido para prática de APIs assíncronas com FastAPI, autenticação JWT e aplicação de boas práticas de arquitetura backend.

---

## 📸 Preview da API

<p align="center">
  <img src="assets/swagger-preview.png" width="900">
</p>

## 👨‍💻 Autor

Regis de Paula
