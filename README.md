# Flix App - Frontend

Frontend desenvolvido em **Streamlit** para consumir a API de gerenciamento de filmes e críticas **Flix API**.

Este aplicativo permite visualizar e gerenciar:
- Filmes
- Atores
- Gêneros
- Avaliações (Reviews)

## 📚 Documentação da API

A API utilizada por este aplicativo possui documentação Swagger disponível em:
👉 **[Swagger UI - Flix API](https://flixapi.dominio.qzz.io/api/schema/swagger-ui/)**

EndPoint Base: `https://flixapi.dominio.qzz.io/`

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

### Passo a Passo

1. **Clone o repositório** (se aplicável) ou baixe os arquivos para sua máquina.

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   streamlit run app.py
   ```

5. O aplicativo será aberto automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

## 🔑 Credenciais de Acesso (Teste)

Para testar as funcionalidades do sistema, utilize o seguinte usuário:

- **Usuário:** `usuarioteste`
- **Senha:** `@123456@`

## 📂 Estrutura de Arquivos

Abaixo está a estrutura principal dos arquivos do projeto:

```text
flix-app/
│
├── actors/                 # Módulo de gestão de Atores
│   ├── page.py             # Interface (View)
│   ├── repository.py       # Comunicação com a API
│   └── service.py          # Regra de negócio
│
├── api/                    # Configurações gerais da API
│   └── service.py          # Serviço de Autenticação
│
├── genres/                 # Módulo de gestão de Gêneros
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── home/                   # Página Inicial
│   └── page.py
│
├── login/                  # Módulo de Login
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── movies/                 # Módulo de gestão de Filmes
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── reviews/                # Módulo de gestão de Avaliações
│   ├── page.py
│   ├── repository.py
│   └── service.py
│
├── app.py                  # Ponto de entrada da aplicação (Main)
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/):** Framework para criação de web apps em Python.
- **Python:** Linguagem de programação principal.
- **Requests:** Biblioteca para requisições HTTP.
