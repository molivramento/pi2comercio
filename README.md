# PI2 Comércio

## Sobre
O PI2 Comércio é um projeto de comércio eletrônico simples que permite aos usuários comprar e vender produtos. O projeto está **em andamento** e é desenvolvido em Python e utiliza as bibliotecas Flask, PostgreSQL, Docker, JQuery, Bootstrap e Google Cloud Platform.

## Requisitos
- Python 3.8 ou superior
- pip

## Instalação
1. Clone o repositório do GitHub.
2. Abra o terminal na pasta do projeto.
3. Instale as dependências com o comando:
   ```shell
      pip install poetry
    ```
4. Instale o projeto com o comando:
      ```shell
      poetry install
      ```
5. Inicie o servidor com o comando:
     ```shell
      poetry run uvicorn main:app --reload
      ```


## Uso
Para usar o PI2 Comércio, siga estas etapas:

1. Acesse o site no seu navegador.
2. Crie uma conta ou faça login com uma conta existente.
3. Navegue pelos produtos disponíveis.
4. Adicione os produtos que deseja comprar ao seu carrinho.
5. Finalize a compra.

## Contribuir
Contribuições são bem-vindas! Para contribuir para o projeto, siga estas instruções:

1. Forneça um relatório de bug ou solicitação de recurso.
2. Envie uma pull request com as suas alterações.

## Funcionalidades
- Listagem de produtos
- Detalhes do produto
- Carrinho de compras
- Finalização da compra
- Filtro de produtos
- Pesquisa de produtos
- Compras recorrentes
- Recomendações de produtos

## Tecnologias
- Python 3.8 ou superior
- Flask
- PostgreSQL
- Docker
- JQuery
- Bootstrap
- Google Cloud Platform

## Containers
- Windows: [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)
- Mac: [https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)
- Linux (baseado em Ubuntu): [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)

Para iniciar os containers, abra a pasta do projeto no terminal e execute os seguintes comandos:
  ```shell
    docker-compose up -d --build
  ```





   
   
