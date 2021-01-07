# Site do PUGPE: Python User Group - Pernambuco

Descrição

### Pre-requisitos

* [Python](https://www.python.org/) na versão 3.9.0 ou superior
* [Poetry](https://python-poetry.org/) para gerenciamento de dependências

### Execução

1. Clonar o projeto: `git clone https://github.com/pugpe/pugpe-site.git`
2. Entrar na pasta raiz do projeto: `cd pugpe-site`
3. Configurar as envs (preencher os valores caso necessário): `mv .env-example .env`
4. Instalar as dependências: `poetry install`
5. Ativar a virtual environment: `poetry shell`
6. Atualizar o schema do banco: `python manage.py migrate`
7. Executar o projeto: `python manage.py runserver`

Após seguir os passos, voce será capaz de acessar http://127.0.0.1:8000/
