import json

import requests


class Scryfall:
    """Represent the Scryfall API service."""

    NAME = 'Scryfall'
    BASE_URL = 'https://api.scryfall.com'
    CARDS_URL = BASE_URL + '/cards/named?'
    REQUEST_DELAY = 10  # seconds

    def __init__(self, data_path):
        self.local_data_file = data_path.joinpath(f'{self.NAME.lower()}.json')
        # Create file to store card data.
        try:
            # Try to open file to check if it does exist.
            with open(self.local_data_file, 'r', encoding='utf-8') as _:
                pass
        except FileNotFoundError:
            # Create file if it does not exist.
            # Dump empty dictionary to enable loading json.
            with open(self.local_data_file, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def __str__(self):
        """Return API string representation."""
        return f'{self.NAME} ({self.BASE_URL})'

    @classmethod
    def get_cards_query_string(cls, name, is_exact=True):
        """Get query string to search for specific named card.

        Name parameter is case insensitive, even if performing exact
          search.
        """
        if is_exact:
            return f'{cls.CARDS_URL}exact={name}'
        return f'{cls.CARDS_URL}fuzzy={name}'

    def get_card_data(self, query_name, expansion=None):
        """Return card data as dictionary."""
        # Todo: Enable expansion as query parameter.
        card_data = self.get_local_card_data(query_name=query_name)

        if card_data is None:
            # Request card data from API service.
            card_data = self._request_card_data(query_name=query_name)
            if card_data is not None:
                # Check that exact name does not exist locally.
                local_card_data = self.get_local_card_data(
                    query_name=card_data['name'].lower())
                if not local_card_data:
                    # Save card data locally first time it is requested.
                    self._save_card_data(card_data=card_data)
        return card_data

    @classmethod
    def _request_card_data(cls, query_name):
        """Request card data from API service."""
        try:
            response = requests.get(
                cls.get_cards_query_string(name=query_name, is_exact=False))
            # Raise exception if "bad" response code.
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return None
        return response.json()

    def get_local_card_data(self, query_name=None):
        """Return card data stored locally as dictionary."""
        # Get all data in local file.
        with open(self.local_data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if query_name is None:
            return data

        # Get specified card data or return None.
        return data.get(query_name.lower(), None)

    def _save_card_data(self, card_data):
        """Save requested card data locally.

        Assume card data has key "name".
        """
        card_name = card_data['name']
        data = self.get_local_card_data()
        data.update({card_name.lower(): card_data})
        with open(self.local_data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print(f'Successfully saved card data for {card_name} to local file.')
