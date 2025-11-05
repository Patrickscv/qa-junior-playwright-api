
# Automação de Testes de API GoRest com Playwright e Python

Este repositório contém um framework de automação para testes de API RESTful, focado no serviço **GoRest**. A automação é desenvolvida em **Python** utilizando a biblioteca **Playwright** (`APIRequestContext`).

---

### Pré-requisitos

Certifique-se de ter o **Python 3** e o **pip** instalados em sua máquina.

### 1. Configuração do Projeto e Instalação

Siga os passos abaixo para preparar o ambiente de execução:

#### **Passo 1: Configurar Variáveis de Ambiente (Token de Acesso)**

O GoRest requer um token de acesso para a maioria das operações (POST, PUT, DELETE).

1.  Localize o arquivo `.env.exemplo` na raiz do projeto.
2.  Abra o arquivo e preencha o campo `ACCESS_TOKEN` com o seu token pessoal, obtido ao criar uma conta no [GoRest API](https://gorest.co.in).
3.  **Renomeie** o arquivo de `.env.exemplo` para `.env` (apenas).

#### **Passo 2: Clonar e Navegar**

1.  Navegue até a pasta principal do projeto no seu terminal:
    ```bash
    cd GoRest_API_Automation-main
    ```

#### **Passo 3: Configurar o Ambiente Virtual**

1.  Crie o ambiente virtual (venv):
    ```bash
    python -m venv venv
    ```
2.  Ative o ambiente virtual:
    * **Windows (PowerShell):**
        ```bash
        .\venv\Scripts\Activate.ps1
        ```
    * **Linux e macOS:**
        ```bash
        source venv/bin/activate
        ```

#### **Passo 4: Instalar Dependências**

1.  Instale todas as bibliotecas Python listadas no `requirements.txt`, incluindo o Playwright:
    ```bash
    pip install -r requirements.txt
    ```
2.  (Opcional, se o Playwright não estiver no `requirements.txt`):
    ```bash
    pip install playwright
    ```

---

### 2. Execução dos Testes

Certifique-se de que você está na pasta do projeto (`GoRest_API_Automation-main`) e com o ambiente virtual **ativado**.

| Comando | Descrição |
| :--- | :--- |
| `pytest` | Executa **todos** os testes de API. |
| `pytest --log-cli-level=INFO` | Executa os testes e exibe os **logs** detalhados (incluindo informações de requisição/resposta, se configurado) no terminal. |
| `pytest -k "nome_do_teste"` | Executa apenas os testes que contêm o texto `"nome_do_teste"` no nome. |

---

### 3. Estrutura do Projeto

* `tests/`: Contém os arquivos de teste de API (ex: `test_users.py`, `test_posts.py`).
* `fixtures/`: Onde podem ser configuradas as *fixtures* do Pytest, como o `APIRequestContext` do Playwright.
* `utils/`: Módulos com funções de ajuda ou dados de *payloads*.
* `requirements.txt`: Lista de dependências do Python.
* `.env`: Arquivo de variáveis de ambiente com o `ACCESS_TOKEN`.
Para ver os logs de cada teste utilize o comando:

pytest --log-cli-level=INFO

