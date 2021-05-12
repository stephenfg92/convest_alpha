import sqlite3

def create_db(db_name):
    conn = sqlite3.connect(db_name)

    c = conn.cursor()

    try:
        # Criar tabela 'acoes'
        c.execute('''CREATE TABLE acoes
            (
                [id] integer PRIMARY KEY AUTOINCREMENT, 
                [nome] text NOT NULL, 
                [ticker] text NOT NULL, 
                [habilitado] integer NOT NULL CHECK (habilitado IN (0, 1) )
            );'''
        )

        # Criar tabela 'fechamentos'
        c.execute('''CREATE TABLE fechamentos
            (
                [id] integer PRIMARY KEY AUTOINCREMENT, 
                [data] date NOT NULL,
                [fechamento] real NOT NULL,
                [acao_id] integer NOT NULL, 
                FOREIGN KEY (acao_id)
                    REFERENCES acoes (id)
            );'''
        )

        # Inserindo valores solicitados

        # Brasil, Bolsa, Balcão
        c.execute('''INSERT INTO acoes (nome, ticker, habilitado) VALUES('Brasil Bolsa Balcao', 'B3SA3.SAO', 1)''')
        # Petroleo Brasileiro
        c.execute('''INSERT INTO acoes (nome, ticker, habilitado) VALUES('Petroleo Brasileiro', 'PETR4.SAO', 1)''')

        conn.commit()
        print('Banco de dados criado com sucesso!')

    except Exception as e:
        print('O programa encontrou um erro: {erro}'.format(erro = e))

    finally:
        conn.close()