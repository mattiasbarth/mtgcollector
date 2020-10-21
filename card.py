import settings


class Card:
    """Represent a (physical) card."""
    CARDS_PATH = settings.CARDS_PATH

    def __init__(self, name, set_):
        """Set up default card data.

        Use set_ for card set to avoid overriding the inbuilt Python set
          constructor.
        """
        # Minimum data to identify card.
        self.name = name
        self.set = set_

        # User submitted data unique to a physical card.
        self.lang = 'en'
        self.condition = 'ex'
        self.is_foil = False
        self.is_signed = False
        self.has_stamp = False
        self.is_alt_art = False
        self.notes = ''

    def __str__(self):
        return f'{self.name} ({self.set})'

    def add_physical_data(
            self,
            lang=None,
            condition=None,
            is_foil=None,
            is_signed=None,
            has_stamp=None,
            is_alt_art=None,
            notes=None,
    ):
        """Add physical card data if specified."""
        if lang is not None:
            self.lang = lang
        if condition is not None:
            self.condition = condition
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

    def add_to_collection(self):
        data = f'{self.name};{self.set}'.lower()
        print(data)
        with open(type(self).CARDS_PATH, 'a', encoding='utf-8') as f:
            f.write(data + '\n')

if __name__ == '__main__':
    card = Card('Cast Out', 'Amonkhet')
    card2 = Card('Cast Out', 'Commander 2020')
    print(card)
    print(card2)
    card.add_to_collection()
    card2.add_to_collection()
