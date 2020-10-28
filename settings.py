import pathlib


# Project root.
import api

ROOT_PATH = pathlib.Path(__file__).parent

# Storing data.
CARDS_DATA_PATH = ROOT_PATH.joinpath('data')  # Todo: Use database.
API = api.Scryfall(CARDS_DATA_PATH)

# Collection.
COLLECTION_PATH = ROOT_PATH.joinpath('collection')
COLLECTION_FILE = COLLECTION_PATH.joinpath('collected.json')
