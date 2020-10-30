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
    pass


def browse_collection():
    """Browse collection by prompting user for card name."""
    pass


if __name__ == '__main__':
    main()
