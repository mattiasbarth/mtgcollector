import json


class Collection:
    """Represent a collection of cards."""

    def __init__(self, path, name):
        """Create new file to store cards, only if it doesn't exist.

        Each collection has a name that must be unique. Cards can belong
          to multiple collections, ie Vampires, Angels, Collected.
        """
        self.name = name
        file_name = f'{self.name.lower()}.json'
        path = path.joinpath(file_name)
        try:
            # Try to open file to make sure it does not exist.
            with open(path, 'r', encoding='utf-8') as _:
                pass
        except FileNotFoundError:
            # Create file if it does not exist.
            # Dump empty dictionary to enable loading json.
            with open(path, 'w', encoding='utf-8') as f:
                json.dump({}, f)
        self.path = path

    def get(self):
        """Return collection data as dictionary."""
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def update(self, edited_data):
        """Update collection with edited data."""
        # Todo: Backup before writing?
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(edited_data, f)

    def browse(self, card_name, expansion=None):
        """Browse collection and return result as a tuple with card
          objects.
        """
        # Todo: Implement this
        # Todo: Enable more search parameters, ie condition
        return self.get().get(card_name.lower(), [])
