# Kanban  Data 
<img src="screenshot/graphiql.png" alt="Tela principal">

> API GraphQL que fornece os dados dos projetos para a aplicação web de gerenciamento de projetos usando o método Kanban. Este backend foi desenvolvido utilizando as seguintes tecnologias: Python 3, FastAPI, Strawberry GraphQL, SQLAlchemy, Asyncio e banco de dados Postgres.

> Esta API foi desenvolvida como uma parte do trabalho de conclusão do terceiro e último módulo - Desenvolvimento Backend Avançado - da Pós-Graduação em Desenvolvimento FullStack da PUC-RIO. 


## Funcionalidades

- [x] Listar quadros (Query boards).
- [x] Consultar quadro (Query board).
- [x] Listar prioridades (Query priorities).
- [x] Consultar tarefa (Query task).
- [x] Adicionar quadro (Mutation addBoard).
- [x] Adicionar prioridade (Mutation addProority).
- [x] Adicionar tarefa (Mutation addTask).
- [x] Atualizar tarefa (Mutation updateTask).
- [x] Deletar tarefa (Mutation deleteTask).
- [x] Adicionar sub tarefa (Mutation addSubTask).
- [x] Marcar subtarefa como pronta (Mutation markSubTaskDone).
- [x] Deletar subtarefa (Mutation deleteSubTask).

## Todo

- [ ] Criar model para o usuário e evitar de usar o ID do Back4app
- [ ] Autenticação/Autorização via serviço de gerência de usuário ou api gateway

## 💻 Pré-requisitos

Antes de começar, verifique se o seu ambiente atende aos seguintes requisitos:

> ATENÇÃO, este backend foi desenvolvido para rodar em conjunto com o frontend (Kanban-Frontend), o serviço de gerenciamento de usuários (Back4app) e um banco de dados Postgres. Recomendo seguir as instruções contidas no README do repositório de implantação - https://github.com/bpbastos/kanban-ms - para garantir uma configuração adequada.

* `Docker`

> Instalação do docker: https://docs.docker.com/engine/install/

## 🚀 Rodando

Faça clone do projeto:
```
git clone https://github.com/bpbastos/kanban-ms.git
```

Acesse o diretório do projeto com:
```
cd kanban-ms/kanban-data
```

Crie um arquivo .env na raiz do diretório kanban-data com as seguintes variáveis:

```env
KANBANFRONT_URL=http://localhost:3000
POSTGRES_HOST=db
POSTGRES_USER=kanban
POSTGRES_PASSWORD=kanbanpass
POSTGRES_DB=kanban
```

No diretório kanban-data em um terminal, execute:
```sh
docker run -d --env-file ./.env -p 5432:5432 --name db postgres:16 
docker build -t kanban-data:1.0 .
docker run -d --env-file ./.env --link db:db -p 8000:8000 --name data kanban-data:1.0 
docker exec --env-file ./.env data python create_db.py
```

Abra o endereço http://localhost:8000/graphql no seu navegador.