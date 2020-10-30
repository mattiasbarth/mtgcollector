from settings import COLLECTION
from card import Card, CardTemplate


def main():
    print('*** MTGCollector ***\n')
    while True:
        print('1. Add a card (add)',
              '2. Browse collection (browse)',
              '3. Exit (exit)',
              sep='\n')
        option = input('Choose an option: ').lower()
        print()
        if option in ('add', '1'):
            add_card()
        elif option in ('browse', '2'):
            # Browse collection.
            browse_collection()
            print()
        else:
            if input('Do you wish to exit (y/n) ').lower() == 'y':
                break


def add_card():
    """Add one or more cards to collection."""
    while True:
        # Prompt user for a card name as long at card name is invalid.
        # Query name can be inexact and is case insensitive but may only
        #   be interpreted  as exactly one card, it can't be ambiguous.
        query_name = input('Name a card: ')
        print(f'Looking for {query_name} in the Multiverse...')
        try:
            card_template = CardTemplate(query_name)
        except ValueError as e:
            print(e, 'Please try again.')
            continue
        break
        # Query name is valid and a card has been found.
    print(f'Found card {card_template.name}!')
    count = input(
        f'How many {card_template.name} do you want to add (1 is default) ')
    count = count.strip() or 1  # Todo: Check if numeric
    for _ in range(int(count)):
        # Prompt user for card expansion, it can't be empty.
        while True:
            # Use previous expansion as default when adding
            #   additional cards.
            default_message = (f'({card_template.expansion.title()} is default)'
                               if card_template.expansion else '')
            expansion = input(f'Expansion{default_message}: ').strip()
            # Todo: Check expansion validity.
            card_template.expansion = expansion or card_template.expansion
            if card_template.expansion:
                break
        # User has entered "valid" expansion.
        # Ask user for specific card data.
        language = input('Language (en is default): ')
        condition = input('Condition (ex is default): ')
        is_foil = input('Foil (y/n, n is default): ')
        is_signed = input('Signed (y/n, n is default): ')
        is_alt_art = input('Alt art (y/n, n is default): ')
        notes = input('Notes: ')
        card_template.set_specific_data(
            language,
            condition,
            is_foil,
            is_signed,
            is_alt_art,
            notes,
        )
        card = Card(card_template.__dict__)
        card.add_to_collection(COLLECTION)
        print(f'Card {card} added to collection {COLLECTION.name}!')
        print()


def browse_collection():
    """Browse collection by prompting user for card name."""
    pass


if __name__ == '__main__':
    main()
