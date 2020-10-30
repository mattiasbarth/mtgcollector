# mtgcollector
A [Magic: The Gathering](https://magic.wizards.com/en/magic-gameplay) card collection application built in Python.

## About
As a collector of MTG cards I want to have to organise my collection. While I use different online services I wanted to build my own local offline solution.
#### Initial features
* User can add card to collection
* Card data is fetched with an API and stored locally
* User can browse collection based on card name (and optionally expansion)

## Installation
Create a new virtual environment then install the requirements.
```
python3 -m pip install -r requirements.txt
```
Set paths to store local API data and collection in `settings.py`. This must be done before running the program and it will crash if either of these paths (as in directories, files will be generated) does not exist.

## Usage
```
python3 -m mtgcollector
```
### Add Card
```
1. Add a card (add)
2. Browse collection (browse)
3. Exit (exit)
Choose an option: 1

Name a card: ightning bol
Looking for ightning bol in the Multiverse...
Successfully saved card data for Lightning Bolt to local file.
Found card Lightning Bolt!
How many Lightning Bolt do you want to add (1 is default): 2
Expansion: Revised
Language (en is default): 
Condition (ex is default): fn
Foil (y/n, n is default): 
Signed (y/n, n is default): 
Alt art (y/n, n is default): 
Notes: 
Card Lightning Bolt (Revised, en) Fn added to collection Collected!

Expansion (Revised is default): Beta
Language (en is default): 
Condition (fn is default): nm
Foil (y/n, n is default): 
Signed (y/n, n is default): 
Alt art (y/n, n is default): 
Notes: 
Card Lightning Bolt (Beta, en) NM added to collection Collected!

```

### Browse Collection
```
1. Add a card (add)
2. Browse collection (browse)
3. Exit (exit)
Choose an option: 2

Card name: lightning bolt
Found 2 cards in Collected
	Lightning Bolt (Revised, en) Fn
	Lightning Bolt (Beta, en) NM

```
