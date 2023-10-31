# API de Consumo de Bancos de Dados Pequenos (Versão Inicial)

## Visão Geral

Esta é uma API desenvolvida como a primeira versão de um sistema projetado para consumir e gerenciar bancos de dados pequenos, que armazenam informações em formato JSON. A API permite criar, listar, atualizar e excluir registros em um banco de dados SQLite. É particularmente útil para aplicativos que lidam com bancos de dados menores e retornam dados em formato JSON.

## Tecnologias e Bibliotecas Principais

As principais tecnologias e bibliotecas utilizadas neste projeto são:

- **SQLite3**: Para criar e gerenciar o banco de dados local onde os registros são armazenados.

- **Flask**: Um framework web em Python que permite criar APIs web de forma simples e eficiente.

- **JSON**: Utilizado para a manipulação de dados no formato JSON.

## Funcionalidades

- **Criação de Tabelas**: A API permite a criação de tabelas no banco de dados SQLite, definindo suas colunas.

- **Inserção de Registros**: É possível inserir registros em tabelas, especificando informações como nome, categoria, tabelas associadas, data de criação e um arquivo binário.

- **Listagem de Registros**: A API fornece endpoints para listar todos os registros armazenados em formato JSON.

- **Filtragem por Categoria**: Os registros podem ser filtrados com base em suas categorias.

- **Leitura de Dados**: A API permite a leitura de dados armazenados, incluindo a capacidade de obter os registros em formato JSON.

- **Atualização de Registros**: É possível atualizar registros existentes com base em seu ID.

- **Exclusão de Registros**: Registros podem ser excluídos com base em seu ID.

## Uso dos Endpoints

A API oferece os seguintes endpoints para interagir com o banco de dados:

- **`/list_sheet` (Método `GET`)**: Retorna uma lista de todos os registros armazenados em formato JSON. Isso permite uma visão geral de todos os dados disponíveis.

- **`/category/<string:categoria>` (Método `GET`)**: Retorna registros com base na categoria especificada em formato JSON. Isso permite a filtragem dos registros por categoria.

- **`/sheet/<int:ID>` (Método `GET`)**: Retorna um registro com base no ID fornecido em formato JSON. Pode opcionalmente aceitar o parâmetro 'TABLE' para especificar uma tabela associada.

- **`/sheet/<int:ID>` (Método `PUT`)**: Permite atualizar um registro existente com base no ID fornecido. Os dados a serem atualizados são passados como parâmetros na solicitação.

- **`/sheet/<int:ID>` (Método `DELETE`)**: Permite excluir um registro com base no ID fornecido. O registro será removido permanentemente do banco de dados.

Esses endpoints tornam a API flexível e capaz de fornecer diferentes funcionalidades de acordo com as necessidades do aplicativo que a consome.

## Execução do Aplicativo

O aplicativo Flask é executado localmente na porta 5000 e pode ser acessado via HTTP. Ele fornece endpoints para interagir com o banco de dados, facilitando a manipulação de registros.

Espero que esta explicação sobre o uso dos endpoints esclareça como a API interage com o banco de dados e fornece acesso aos dados armazenados.

## Como instalar o repositório

Após baixar todos os arquivos, rode os seguintes comandos no Terminal deste diretório:

```
python -m venv virtual
virtual/Scripts/activate
pip install -r requirements.txt
```