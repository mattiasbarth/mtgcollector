import json


class Collection:
    """Represent a collection of cards."""

    def __init__(self, path, name):
        self.path = path
        self.name = name

        # Create file to store cards.
        file_name = f'{self.name.lower()}.json'
        try:
            # Try to open file to make sure it does not exist.
            with open(file_name, 'r', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            # Create file if it does not exist.
            # Dump empty dictionary to enable loading json.
            with open(
                    self.path.joinpath(f'{self.name.lower()}.json'), 'w',
                    encoding='utf-8') as f:
                json.dump({}, f)
        else:
            raise FileExistsError(
                f'A collection with the name {self.name} already exists,'
                ' please chose another name.')


def main():
    pass


if __name__ == "__main__":
    main()
