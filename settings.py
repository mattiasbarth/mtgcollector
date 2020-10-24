import pathlib

ROOT_PATH = pathlib.Path(__file__).parent
# DATA_PATH = ROOT_PATH.joinpath('data')
COLLECTION_PATH = ROOT_PATH.joinpath('collection')
CARDS_PATH = COLLECTION_PATH.joinpath('cards.json')
