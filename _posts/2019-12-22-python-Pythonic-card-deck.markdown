---
layout: post
title: A pythonic Card Deck
date: 2019-12-22 21:10:24.000000000 +09:00
tags: python
---

Referenced from Luciano Ramalho, 'Fluent Python'

Example:

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spades diamonds clubs heart'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, _cards)
        return self._cards[positions]
```

### collections.nametuple()

Create a class named with 'Card', which has two attributes, 'rank' and 'suit', when you call this class and transfer the atrributes, the order of the atrribute should be the same with defined atrribute.

Which is used to build classes of objects that are just the bundles of attributes with no custom methods, like a database record.

```python
# Card = collections.namedtuple('Card', ['rank', 'suit'])
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
```

### len() of the 'FrenchDeck'

```python
>>> deck = FrechDeck()
>>> len(deck)
52
```

### Reading specific cards from the deck

```python
# suits = 'spades diamonds clubs hearts'.split()
# ranks = [str(n) for n in range(2, 11) + list('JQKA')]
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
```

### Using random.choice to pick a random card

```python
>>> from random import choice
>>> choice(deck)
Card(rank='3', suit='hearts')
>>> choice(deck)
Card(rank='K', suit='spades')
```

### \_\_getitem\_\_() makes FrenchDeck implement the slice and iterable

```python
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]
```

```python
>>> for card in deck:
        print(card)
...
Card(rank='2', suit='spades')
...
```

```python
>>> for card in reversed(deck):
        print(card)
...
Card(rank='A', suit='hearts')
```
### 'in' instead of \_\_contains\_\_method

'in' operator does a sequential scan, and **'in' works with FrenchDeck class because it it iterable.

```python
>>> Card('Q', 'hearts') in deck
True
>>> Card('7', 'beasts') in deck
False
```

### Sorting of FrenchDeck

```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

>>> for card in sorted(deck, key=spades_high):
        print(card)
...

```

### Summary

By implementing the special methods \_\_len\_\_ and \_\_getitem\_\_, our FrenchDeck behaves like a standard Python sequence, allowing it to benefit from **core language features** (e.g., iteration and slicing) and **from the standard library**, as shown by the examples using random.choice, reversed and sorted. Thanks to composition, the \_\_len\_\_ and \_\_getitem\_\_ implementations can hand off all the work to a list object, self.\_cards.



