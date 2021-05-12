from pathlib import Path
import os

API_KEY = "KHU49FD8HOHZII9L"

SYMBOL_LIST = ['B3SA3.SAO', 'PETR4.SAO']

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
DB_PATH = str(Path(__file__).resolve()).replace(filename, '')
DB_NAME = 'Fechamentos.db'

