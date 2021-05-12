from constants import API_KEY, SYMBOL_LIST, DB_PATH, DB_NAME
from data import get_default_values
from db_operations import insert_defaults

if __name__ == "__main__":
    try:
        query = {}

        for symbol in SYMBOL_LIST:
            result = get_default_values(symbol, API_KEY)
            query[symbol] = result

        db = ''.join(DB_PATH + DB_NAME)
        insert_defaults(db, query)

        print("Operação concluída com sucesso.")
        

    except Exception as e:
        print('O programa encontrou um erro: {erro}'.format(erro = e))