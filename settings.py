import pathlib

import api
import collection


# Project root.
ROOT_PATH = pathlib.Path(__file__).parent

# Storing data.
CARDS_DATA_PATH = ROOT_PATH.joinpath('data')  # Todo: Use database.
API = api.Scryfall(CARDS_DATA_PATH)

# Collection.
COLLECTION_PATH = ROOT_PATH.joinpath('collection')
COLLECTION = collection.Collection(COLLECTION_PATH, name='collected')
