
**1. Configurando váriaveis de ambiente:**

Antes de rodar, é necessário configurar o arquivo .env.example com as credenciais da API:

Abra o arquivo .env.exemplo e preencha o campo "ACCESS_TOKEN" com seu token de acesso obtido ao criar uma conta no gorest.api

Em seguida renomeie esse arquivo de ".env.exemplo" para ".env" apenas.

**2. Como realizar a instalação:**

Em seu terminal, navegue até a pasta do projeto:

cd qa-junior-playwright-api
Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:

PowerShell: .\venv\Scripts\Activate.ps1

No Linux e Mac: source venv/bin/activate

Instale as dependências:

Retorne para a pasta principal onde está o requirements.txt
cd ..

pip install -r requirements.txt

Instale o Playwright:

playwright install

**3. Execução dos Testes**

Na pasta do projeto (cd qa-junior-playwright-api)

Com o ambiente virtual ativado e o arquivo .env configurado, execute o Pytest:

pytest

Para ver os logs de cada teste utilize o comando:

pytest --log-cli-level=INFO

