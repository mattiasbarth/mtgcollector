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
        #   be interpreted as exactly one card, it can't be ambiguous.
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
        f'How many {card_template.name} do you want to add (1 is default): ')
    count = count.strip() or 1  # Todo: Check if numeric
    for _ in range(int(count)):
        # Prompt user for card expansion, it can't be empty.
        while True:
            # Use previous expansion as default when adding
            #   additional cards.
            default_message = (
                f'({card_template.expansion.title()} is default)'
                if card_template.expansion else '')
            expansion = input(f'Expansion {default_message}: ').strip()
            # Todo: Check expansion validity
            card_template.expansion = expansion or card_template.expansion
            if card_template.expansion:
                # Expansion is valid.
                break
        # Ask user for specific card data.
        # Todo: Move handling specific card data to Card class from
        #   CardTemplate?
        language = input(f'Language ({card_template.language} is default): ')
        condition = input(f'Condition ({card_template.condition} is default): ')
        # Todo: Add option to fill in extras or not
        is_foil = input(
            f"Foil (y/n, {'y' if card_template.is_foil else 'n'} is default): ")
        is_signed = input(
            f"Signed (y/n, {'y' if card_template.is_signed else 'n'} is default): ")
        is_alt_art = input(
            f"Alt art (y/n, {'y' if card_template.is_alt_art else 'n'} is default): ")
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
    # Todo: Enable multiple search parameters
    # Todo: Add loop to enable browsing multiple cards
    # Todo: Enable browsing multiple cards in the same query
    # Todo: Sort result by name, expansion etc
    card_name = input('Card name: ')
    results = [
        Card(card_data=data)
        for data in COLLECTION.browse(card_name)]
    results_count = len(results)
    print(
        f"Found {results_count} card{'s' if results_count != 1 else ''}"
        f' in {COLLECTION.name}')
    for card in results:
        print(f'\t{card}')


if __name__ == '__main__':
    main()
