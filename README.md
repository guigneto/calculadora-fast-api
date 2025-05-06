# 🧮 Calculadora com FastAPI

Este é um projeto simples de API REST usando FastAPI que realiza operações matemáticas básicas: soma, subtração, multiplicação, divisão e exponenciação.

---

## 🚀 Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn
- Pytest

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/guigneto/calculadora-fast-api.git
cd calculadora-fast-api
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install fastapi uvicorn pytest
```

---

## ▶️ Executando a API

Dentro da raiz do projeto, execute:

```bash
uvicorn main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para testar os endpoints via Swagger UI.

---

## ✅ Endpoints disponíveis

| Operação        | Método | Rota              |
|-----------------|--------|-------------------|
| Soma            | POST   | `/soma`           |
| Subtração       | POST   | `/subtracao`      |
| Multiplicação   | POST   | `/multiplicacao`  |
| Divisão         | POST   | `/divisao`        |
| Exponenciação   | POST   | `/exponenciacao`  |

### 📤 Corpo da requisição (JSON):

```json
{
  "a": 10,
  "b": 2
}
```

---

## 🧪 Rodando os testes

Os testes automatizados estão na pasta `tests/`.

Execute com:

```bash
pytest tests/
```

---

## 📁 Estrutura do Projeto

```
calculadora-fast-api/
├──  app/
│   ├── main.py
│   ├── models.py
│   └── operations.py
├── tests/
│   └── test_main.py
```

---

## 📌 Licença

Este projeto é livre para uso educacional e pessoal.