import sqlite3
import os
from datetime import date, datetime
from create_db import create_db

def check_db(db_name):
    if not os.path.isfile(db_name):
        create_db(db_name)

def get_series(conn):
    c = conn.cursor()
    series = {}

    c.execute(''' SELECT * FROM acoes ''')
    series_query = c.fetchall()

    for s in series_query:
        _id = s[0]
        name = s[1]
        ticker = s[2]
        enabled = None

        if s[3] == 0:
            enabled = False
        else:
            enabled = True

        series[ticker] = [enabled, _id]

    return series

def insert_values(stored_series, queried_values, conn):
    c = conn.cursor()

    for ticker in stored_series.keys():
        enabled = stored_series[ticker][0]
        ticker_id = stored_series[ticker][1]

        if enabled:
            values = queried_values[ticker]

            for date in values.keys():
                datetime_obj = datetime.strptime(date, '%Y-%m-%d').date()
                value = values[date]

                c.execute(''' SELECT * FROM fechamentos WHERE data = ? and acao_id = ? ''', (date, ticker_id))
                select = c.fetchall()

                if len(select) > 0:
                    selection_contents = select[0]
                    update_values(date, value, ticker_id, selection_contents, conn)

                else:
                    c.execute(''' INSERT INTO fechamentos (data, fechamento, acao_id) VALUES(?, ?, ?) ''', (datetime_obj, value, ticker_id))
                    conn.commit()

def update_values(date, value, ticker_id, select, conn):
    c = conn.cursor()

    selection_id = select[0]
    selection_date = select[1]
    selection_value = select[2]
    selection_ticker_id = select[3]

    if selection_date == date and selection_ticker_id == ticker_id:
        if selection_value != value:
            c.execute(''' UPDATE fechamentos SET fechamento = ? WHERE acao_id = ? AND data = ?;''', (value, ticker_id, date))
            conn.commit()

def insert_defaults(db_name, queried_values):
    check_db(db_name)

    conn = sqlite3.connect(db_name)

    stored_series = get_series(conn)
    
    insert_values(stored_series, queried_values, conn)

    conn.close()