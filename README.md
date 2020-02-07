# patterns-test-serverless

Exemplo de uso de patterns - Abstract, Singleton, Iterator, Model

As funções simulam uma api para uma vitrine de produtos, com faq, destaques e videos do Youtube

# Conteudo

* Lista de Funcoes
    * cms/estoque?page[number]={page}&page[size]={size}&sort={id|descricao|categoria|valor} listagem de produtos em estoque
    * cms/produto/{id_produto} - dados da instituicao
    * cms/produto/{id_produto}/videos - "embed" para youtube    
    * cms/destaques - destaques da home
    * cms/faq/add - gravar uma pergunta
    * cms/faq/{id_produto} - lista as perguntas e respostas de um produto

# Padrões
> Esta API utiliza os padrões da https://jsonapi.org/

## Sobre ordenação e paginação:

```
O parâmetro "sort" permite uma lista separada por vírgulas. Exemplo: "valor,categoria".
Para indicar ordem decrescente, deve-se informar o sinal de menos "-" antes do nome do campo. Exemplo: "-valor".
O parâmetro "sort" é opcional.
O parâmetro "page[number]", caso não seja informado, será 1.
O parâmetro "page[size]", caso não seja informado, será 25.
```

## Função faq - parâmetros:
| **Campo** | **Tipo** | **Descrição** | **Obrigatório** |
| --------- | -------- | ------------- | --------------- |
|id_produto| Numérico | ID do produto | Sim |
|nome | Texto | Nome do cliente | Sim |
|email | Texto | Email para o cliente receber a resposta | Sim |
|texto | Texto | Mensagem que o cliente digitou | Sim |


# Tecnologias

- Serverless framework
- Python 3
- Sql Server
- Linux
- AWS (caso queira fazer deploy. Os exemplos podem ser executados localmente.)

### Pré-requisitos

São necessários para execução:

```
Npm - instalação dos pacotes utilizados
Serverless - realização do deploy na AWS
Python3 - linguagem de codificação
Pip3 - instalador de pacotes do python
libsysbdb.so5 - biblioteca utilizada pelo pymssql para acessar o SQL Server
```

### Instalação

Instalar o NodeJS:

```
apt-get install nodejs
```

Instalar o NPM:

```
apt-get install npm
```

Navegar na raíz do projeto e instalar as dependências listadas no packpage.json

```
npm i
```

Instalar bibliotecas dependentes para o projeto

```
pip3 install -r requirements.txt pode ser necessário executar como adm/root
```

### Editando

Realizar alterações dentro do arquivo..

```
serverless.yml
```

.. como nome da api, dos modulos etc..., ficando apto para a realização do deploy.


## Deploy

Para a realização do deploy na AWS é necessário rodar os seguintes comandos:

Criar Estrutura:
```
serverless deploy --stage=<stage> -v
```

Remover Estrutura:
```
serverless remove --stage=<stage> -v
```

## Exemplos

Antes de executar um teste, abra o arquivo src/config.ini e preencha as informações pedidas, como a base de dados.

Abra o arquivo serverless.yml e modifique as configurações que achar necessárias.

O script de criação das tabelas está no arquivo test/database_script.sql.

Para executar um teste, use o comando:

```
serverless invoke local -f <nome-da-funcao>
```

Com parâmetros:

```
serverless invoke local -f <nome-da-funcao> -p test/<nome-do-arquivo-json>.json
```

## Autor

* **Telma Neu**

## Versões

1.0.0 - patterns example
