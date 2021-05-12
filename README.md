# Teste proposto pela Convest Investimentos

Esse repositório contém o código fonte do programa desenvolvido afim de cumprir o teste proposto pela Convest Investimentos. Este repositório serve como forma de avaliação para minha possível contratação.

A função que o programa exerce é o recolhimento de dados da API disponibilizada pela Alpha Advantage. Os dados recolhidos são referentes aos valores de fechamento diários das ações da Petrobrás e da B3, limitados aos valores divulgados na semana anterior a execução do programa. Os dados são então processados e inseridos em um banco de dados criado automaticamente. Caso seja necessário, o programa também fará reconciliação com dados pré-existentes.

## Instruções para instalação

### 1. Clone o repositório

Basta usar o comando `git clone https://github.com/stephenfg92/convest_alpha.git` em seu terminal.

### 2. Crie um virtual enviroment para o projeto.

Navegue até a pasta onde o repositório foi clonado e use o comando `python -m venv venv/`

### 3. Ative o virtual environment

Se estiver em um abiente Windows, use o seguinte comando: `venv\Scripts\activate`

Se estiver em um ambiente Linux, use o seguinte comando: `source venv/Scripts/activate`

### 4. Instale as dependências necessárias

Para instalar as dependências necessárias, navegue até a pasta raíz do projeto e use o comando `pip install -r requirements.txt`

## Intruções para uso

Para utilizar o programa, substitua o valor da variável API_KEY, localizada em Src/constants.py, pelo valor de sua chave pessoal da API Alpha Advantage. Essa variável deve obrigatoriamente ser uma string, portanto a chave deverá ser escrita entre aspas.

Alternativamente, é possível criar uma variável de ambiente em seu sistema e usá-la como valor desta variável. Ex.: `API_KEY = os.environ.get('API_KEY')`

Com a chave da API configurada, basta executar o script Src/main.py. 

Caso não haja um banco de dados pronto para receber as informações da API, o programa criará um novo banco automaticamente no diretório Src. O endereço e o nome do banco de dados podem ser configurados no script Src/constants.py, bastando alterar as variáveis DB_PATH e DB_NAME conforme a preferência do usuário.

## Algumas considerações

### Modelagem de dados

O banco de dados criado pelo programa usa o seguinte modelo:

```
CREATE TABLE acoes
            (
                [id] integer PRIMARY KEY AUTOINCREMENT,
                [nome] text NOT NULL,
                [ticker] text NOT NULL,
                [habilitado] integer NOT NULL CHECK (habilitado IN (0, 1) )
            );

CREATE TABLE fechamentos
            (
                [id] integer PRIMARY KEY AUTOINCREMENT,
                [data] date NOT NULL,
                [fechamento] real NOT NULL,
                [acao_id] integer NOT NULL,
                FOREIGN KEY (acao_id)
                    REFERENCES acoes (id)
            );

```

Observe que o campo ticker da tabela acoes(ações) está diretamente associado aos campos id, nome e habilitado.

De acordo com a necessidade do cliente, uma terceita tabela contendo apenas o campo ticker e uma referência a tabela de ações poderá ser criada, desassociando estas duas variáveis.

### Acoplamento dos sistemas

O programa é fortemente acoplado ao banco de dados. Isto é, ele faz referência direta aos nomes das tabelas e campos do banco de dados. Deste modo, qualquer alteração na modelagem de dados levará a problemas na execução do código.

Esse problema pode ser resolvido usando algum sistema ORM, ou criando rotinas que considerem que os nomes das tabelas e campos sejam variáveis. Essas soluções podem ser facilmente implementadas de acordo com as necessidades do cliente.

### Orientação a objeto

O paradigma usado no desenvolvimento do programa pode ser facilmente substituído de procedural para orientado a objeto, bastando encapsular o conteúdo dos scripts em classes. Essa solução pode ser implementada de acordo com as necessidades do cliente.

### Considerações finais.

Agradeço o convite para participação do processo de contratação da Convest!

Visite meu site pessoal: stephenfg.com.br.
