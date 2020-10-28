import pathlib


# Project root.
ROOT_PATH = pathlib.Path(__file__).parent

# Persisting data.
API_NAME = 'scryfall'

CARDS_DATA_DIR_PATH = ROOT_PATH.joinpath('data')
CARDS_DATA_FILE = CARDS_DATA_DIR_PATH.joinpath(f'{API_NAME}.json')

COLLECTION_PATH = ROOT_PATH.joinpath('collection')
COLLECTION_FILE = COLLECTION_PATH.joinpath('collected.json')
