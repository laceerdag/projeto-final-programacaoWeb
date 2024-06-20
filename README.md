# Projeto Final - Programação Web

Um projeto web desenvolvido com FastAPI, SQLAlchemy e Jinja2, oferecendo uma API para gerenciar PCs, com endpoints para criar, listar e deletar PCs. Inclui autenticação básica com OAuth2 e senhas hash.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Python 3.7+
SQLite
Docker (opcional)
```

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

1. Clone o repositório:
   ```
   git clone <   git clone <(https://github.com/laceerdag/projeto-final-programacaoWeb.git>>
   cd projeto-final-programacaoweb
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure o banco de dados (será criado automaticamente na primeira execução):
   ```
   python -m app.main
   ```

## ⚙️ Executando os testes

Explicar como executar os testes automatizados para este sistema.

### 🔩 Analise os testes de ponta a ponta

Explique que eles verificam esses testes e porquê.

```
pytest tests/
```

### ⌨️ E testes de estilo de codificação

```
flake8 app/
```

## 📦 Implantação

### Localmente

Para executar o projeto localmente, utilize o comando:

```
uvicorn app.main:app --reload
```

### Usando Docker

Para executar o projeto usando Docker, utilize os seguintes comandos:

```
docker-compose up --build
```

## 🛠️ Construído com


* [FastAPI](https://fastapi.tiangolo.com/) - O framework web usado
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para banco de dados
* [Jinja2](https://palletsprojects.com/p/jinja/) - Template engine
* [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
* [Docker](https://www.docker.com/) - Containerização

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início.

* **Gabriel Costa** - *Trabalho Inicial - back end* - [gabrielcosta]([https://github.com/linkParaPerfil](https://github.com/laceerdag))
* **Lucas ** - *Front-end* - [Lucas]([https://github.com/linkParaPerfil](https://github.com/lucasrso?tab=overview&from=2024-06-01&to=2024-06-20))


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Agradecimentos

* Agradeço ao Professor Lucas por me fazer perder sono 🫂;

---
⌨️ com ❤️ por [Gabriel](https://github.com/laceerdag)) 😊
