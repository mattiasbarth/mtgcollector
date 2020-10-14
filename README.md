# mtgcollector
A [Magic: The Gathering](https://magic.wizards.com/en/magic-gameplay) card collection application built in Python.

## About
As a collector of MTG cards I want to have to organise my collection. While I use different online services I wanted to build my own local offline solution.
#### Initial features
* User can add card to collection
* Card data is fetched with an API and stored locally
* User can browse collection based on card name (and optionally set)

## Installation
Create a new virtual environment then install the requirements.
```
python3 -m pip install -r requirements.txt
```

## Usage
### Add Card
```
python3 -m mtgcollector add  <card name> --exp <set name>
```

### Browse Collection
```
python3 -m mtgcollector browse  <card name> --exp <set name>
```

