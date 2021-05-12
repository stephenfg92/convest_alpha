from pathlib import Path
import os

API_KEY = "API_KEY"

SYMBOL_LIST = ['B3SA3.SAO', 'PETR4.SAO']

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
DB_PATH = str(Path(__file__).resolve()).replace(filename, '')
DB_NAME = 'Fechamentos.db'

