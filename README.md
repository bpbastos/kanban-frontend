# Kanban  Frontend 

[![bpbastos - kanban-frontend](https://img.shields.io/static/v1?label=bpbastos&message=kanban-frontend&color=blue&logo=github)](https://github.com/bpbastos/kanban-frontend "Go to GitHub repo")
[![Package - nuxt](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/nuxt?color=blue)](https://www.npmjs.com/package/nuxt)
[![Package - @nuxtjs/tailwindcss](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/@nuxtjs/tailwindcss?color=blue)](https://www.npmjs.com/package/@nuxtjs/tailwindcss)
[![Package - daisyui](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/daisyui?color=blue)](https://www.npmjs.com/package/daisyui)
[![Package - pinia](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/pinia?color=blue)](https://www.npmjs.com/package/pinia)
[![Package - @pinia/nuxt](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/@pinia/nuxt?color=blue)](https://www.npmjs.com/package/@pinia/nuxt)
[![Package - @nuxtjs/apollo](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/@nuxtjs/apollo?color=blue)](https://www.npmjs.com/package/@nuxtjs/apollo)
[![Package - @nuxtjs/color-mode](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/@nuxtjs/color-mode?color=blue)](https://www.npmjs.com/package/@nuxtjs/color-mode)
[![Package - @pinia-plugin-persistedstate/nuxt](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/@pinia-plugin-persistedstate/nuxt?color=blue)](https://www.npmjs.com/package/@pinia-plugin-persistedstate/nuxt)
[![Package - @vueuse/nuxt](https://img.shields.io/github/package-json/dependency-version/bpbastos/kanban-frontend/@vueuse/nuxt?color=blue)](https://www.npmjs.com/package/@vueuse/nuxt)

<img src="screenshot/board.png" alt="Tela principal">

> Frontend da SPA de gerenciamento de projetos usando o método Kanban. Este frontend foi construído utilizando as tecnologias Nuxt 3, Vue 3, Tailwind CSS e DaisyUI, e se integra com duas APIs distintas. Uma delas é uma API RESTful responsável pelo gerenciamento de usuários, fornecida pelo serviço de BaaS (Backend As A Service) oferecido pelo provedor [Back4App](https://www.back4app.com/). A segunda API é uma API GraphQL fornecida pelo micro-serviço [Kanban Data](https://github.com/bpbastos/kanban-data).

> Link para o [protótipo em alta fidelidade no Figma](https://www.figma.com/file/H1MaexkrCc6AknLQi43HqE/Kanban-App?type=design&node-id=0%3A1&mode=design&t=wljF02F4Yds8ZjUA-1)

> Este frontend foi desenvolvido como uma parte do trabalho de conclusão do terceiro e último módulo - Desenvolvimento Backend Avançado - da Pós-Graduação em Desenvolvimento FullStack da PUC-RIO. 


## Funcionalidades

- [x] Listar quadros.
- [x] Criar novo quadro.
- [x] Criar tarefa.
- [x] Editar tarefa.
- [x] Excluir tarefa.
- [x] Adicionar sub tarefas.
- [x] Login de usuário.
- [x] Logout de usuário.
- [x] Registro de usuários.
- [x] Gerenciador de temas.
- [x] Sistema de notificação.
- [x] Implementar backend real.
      
## Todo

- [ ] Arquivar quadros.
- [ ] Criar/Editar/Arquivar workflows|status.
- [ ] Arquivar tarefas.
- [ ] Reordenar tarefas.
- [ ] Reordenar sub tarefas.
- [ ] Arrastar tarefas entre workflows|status.
- [ ] Layout Responsivo para mobile.
- [ ] Validação dos formulários.
- [ ] Tratamento de erro para consultas graphql.
- [ ] Exibir/Editar informações do perfil de usuário.


## 💻 Pré-requisitos

Antes de começar, verifique se o seu ambiente atende aos seguintes requisitos:

> ATENÇÃO, este frontend requer que o módulo de gerenciamento de usuários do [Back4App](https://www.back4app.com/) e micro serviço de dados [Kanban Data](https://github.com/bpbastos/kanban-data) estejam em execução antes de iniciar. Recomendo seguir as instruções contidas no README do repositório de implantação - [Kanban Deploy](https://github.com/bpbastos/kanban-deploy) - para garantir uma configuração adequada.

* `Docker`

> Instalação do docker: https://docs.docker.com/engine/install/

* `Conta no BaaS - Back4app`

> Você precisa criar uma conta gratuita no Back4app (https://back4app.com) e recuperar as seguintes Keys:

```
APPLICATION_ID
RESTAPIKEY
```

> As Keys estão disponíveis na dashboard administrativa em "App Settings" > "Security & Keys"

## 🚀 Rodando

Faça clone do projeto:
```
git clone https://github.com/bpbastos/kanban-frontend.git
```

Acesse o diretório do projeto com:
```
cd kanban-frontend
```

Crie um arquivo .env na raiz do diretório kanban-frontend com as seguintes variáveis:

> Substituia as variáveis BACK4APP_APPID e BACK4APP_RESTAPIKEY com as keys da sua conta no Back4app. 
> Crie uma chave única de 32 caracteres e atribua à variável NUXT_SECRET.

```env
BACK4APP_URL=https://parseapi.back4app.com
BACK4APP_APPID=chave-appid-do-back4app
BACK4APP_RESTAPIKEY=chave-restapikey-do-back4app
KANBANDATA_URL=http://localhost:8000/graphql
NUXT_SECRET=chave-com-32-caracteres
```

No diretório kanban-frontend em um terminal, execute:
```sh
docker build -t kanban-frontend:1.0 $(for i in `cat .env`; do out+="--build-arg $i " ; done; echo $out;out="") .
```
PS.: O trecho "`$(for i in `cat .env`; do out+="--build-arg $i " ; done; echo $out;out="")`" constrói o parâmetro --build-arg automaticamente de acordo com as variáveis do arquivo .env.

E depois:
```sh
docker run -d --env-file ./.env -p 3000:3000 --name frontend kanban-frontend:1.0 
```

Abra o endereço http://localhost:3000/ no seu navegador.
