import json

import settings


class Card:
    """Represent a collectible card."""

    def __init__(self, query_name):
        """Set up default card data."""

        self.query_name = query_name.lower()
        data = self.get_data()
        if data is None:
            raise ValueError(f'A card with the name {query_name} does not exist'
                             ' in the Multiverse!')

        # Shared card data between expansions.
        self.name = data['name']
        self.cmc = data['cmc']
        self.mana_cost = data['mana_cost']
        self.colors = data['colors']

        # Default user submitted data, unique to each physical card.
        self.expansion = None
        self.language = 'en'
        self.condition = 'ex'
        self.is_foil = False
        self.is_signed = False
        self.has_stamp = False
        self.is_alt_art = False
        self.notes = ''

        self.collection = None

    def __str__(self):
        return f"{self.name} ({self.expansion.title()}) {self.condition}{' *' if self.is_foil else ''}"

    def set_specific_data(
            self,
            language=None,
            condition=None,
            is_foil=None,
            is_signed=None,
            has_stamp=None,
            is_alt_art=None,
            notes=None,
    ):
        """Set specific card data if specified by user."""
        if language is not None:
            self.language = language.lower()
        if condition is not None:
            self.condition = condition.lower()
        if is_foil is not None:
            self.is_foil = is_foil
        if is_signed is not None:
            self.is_signed = is_signed
        if has_stamp is not None:
            self.has_stamp = has_stamp
        if is_alt_art is not None:
            self.is_alt_art = is_alt_art
        if notes is not None:
            self.notes = notes

    def get_data(self):
        """Get card data, either from local file or external API.

        Try to get data from local file, then try the external API to
          avoid unnecessary API requests.
        """
        card_data = self.get_local_data(self.query_name)
        if card_data is None:
            card_data = self.get_api_data(self.query_name)
        return card_data

    @classmethod
    def get_api_data(cls, query_name):
        pass

    @classmethod
    def get_local_data(cls, query_name):
        """Return card data stored locally as dictionary."""
        # Get all data in local file.
        with open(settings.CARDS_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Get specified card data or return None.
        return data.get(query_name, None)

    def add_to_collection(self):
        id_key = f'{self.name};{self.set}'.lower()
        # Try to open file, create it if doesn't exist.
        try:
            with open(settings.COLLECTION_FILE, 'r', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            with open(settings.COLLECTION_FILE, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        with open(settings.COLLECTION_FILE, 'r+', encoding='utf-8') as f:
            pass

if __name__ == '__main__':
    card = Card('Cast Out')
    card2 = Card('Cast Out')
    print(card)
    print(card2)
    card.add_to_collection()
    card2.add_to_collection()
