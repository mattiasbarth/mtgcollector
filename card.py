import settings


class CardTemplate:
    """Represent a template of a collectible card.

    The card template is not an actual card but a kind of
      "data container" that is responsible for validating data before
      a card object is created.
    """

    def __init__(self, query_name):
        """Validate that a card exists."""

        self.query_name = query_name
        data = self.get_data()
        if data is None:
            raise ValueError(f'A card with the name {query_name} does not exist'
                             ' in the Multiverse!')

        self.data = data
        # Shared card data between expansions.
        self.name = data['name']
        self.cmc = data['cmc']
        self.mana_cost = data['mana_cost']
        self.colors = data['colors']

        # Default user submitted data, unique to each physical card.
        self.expansion = ''
        self.language = 'en'
        self.condition = 'ex'
        self.is_foil = False
        self.is_signed = False
        self.has_stamp = False
        self.is_alt_art = False
        self.notes = ''

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
        """Set specific card data specified by user."""
        if language:  # Todo: Validate language
            self.language = language.lower()
        if condition:  # Todo: Validate condition
            self.condition = condition.lower()

        self.is_foil = is_foil.lower() == 'y'
        self.is_signed = is_signed.lower() == 'y'
        self.has_stamp = has_stamp.lower() == 'y'
        self.is_alt_art = is_alt_art.lower() == 'y'
        self.notes = notes or ''

    def get_data(self):
        """Get card data, either from local file or external API.

        Try to get data from local file, then try the external API to
          avoid unnecessary API requests.
        """
        return settings.API.get_card_data(self.query_name)


class Card:
    """Represent a physical collectible card."""

    def __init__(self, card_data):
        """Use valid data from card template to set card data."""
        self.name = card_data['name']
        self.mana_cost = card_data['mana_cost']
        self.cmc = card_data['cmc']
        self.colors = card_data['colors']
        self.expansion = card_data['expansion']
        self.language = card_data['language']
        self.condition = card_data['condition']
        # Temp hack to fix correct case for condition while it's not a
        #   proper class.
        # Todo: Fix!
        self.condition = (self.condition.title()
                          if self.condition.lower() != 'nm'
                          else self.condition.upper())
        self.is_foil = card_data['is_foil']
        self.is_signed = card_data['is_signed']
        self.has_stamp = card_data['has_stamp']
        self.is_alt_art = card_data['is_alt_art']
        self.notes = card_data['notes']

    def __repr__(self):
        return (f'<{self.__class__.__name__} ({self.name}, {self.language})'
                f'{self.condition}>')

    def __str__(self):
        return (f'{self.name} ({self.expansion.title()}, {self.language})'
                f" {self.condition} {' FOIL' if self.is_foil else ''}")

    def add_to_collection(self, collection):
        """Add card to specified collection.

        Although the method belongs to the card, all logic of how to
          add the data belongs to the collection class.
        """
        collection_data = collection.get()

        # Use card name as key to find cards in collection.
        key = self.name.lower()
        card_data = collection_data.get(key, None)
        if card_data is None:
            # A card with the card's name is not in collection; add its
            #   key and assign it to an empty list.
            collection_data[key] = []

        # Card has guaranteed a key in the collection and the new data
        #   can be appended. Easiest way is to use the class' internal
        #   dictionary.
        collection_data[key].append(self.__dict__)
        collection.update(collection_data)
