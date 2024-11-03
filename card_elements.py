from __future__ import annotations

import random

class Card:

    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value
        self.flipped = False

    def flip(self):
        self.flipped = not self.flipped

    def __str__(self):
        return "{0} {1}".format(self.value,self.suit)

    def __gt__(self, other: Card):
        return self.value > other.value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Pile:

    def __init__(self):
        self.cards: list[Card] = []
        self.flipped_count = 0

    def addCard(self, card: Card):
        self.cards.insert(0,card)
        if card.flipped:
            self.flipped_count += 1

    def flipFirstCard(self):
        if len(self.cards)>0:
            self.cards[0].flip()
            self.flipped_count += 1 if self.cards[0].flipped else -1

    def getFlippedCards(self):
        return [card for card in self.cards if card.flipped]

    def __str__(self):
        returnedCards = [str(card) for card in reversed(self.getFlippedCards())]
        flippedDownCount = len(self.cards) - len(self.getFlippedCards())
        if flippedDownCount>0:
            returnedCards.insert(0,"{0} cards flipped down".format(flippedDownCount))
        return ", ".join(returnedCards)

class Deck:

    def __init__(self, values, suits):
        self.cards: list[Card] = []
        self.cache = []
        self.populate(values,suits)
        self.shuffle()

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])

    def populate(self, values, suits):
        for suit in suits:
            for value in values:
                thisCard = Card(suit,value)
                self.cards.append(thisCard)

    def shuffle(self):
        random.shuffle(self.cards)

    def getFirstCard(self):
        if len(self.cards)>0:
            return self.cards[0]
        else:
            return None

    def takeFirstCard(self, flip=True):
        if len(self.cards)>0:
            nextCard = self.cards.pop(0)
            if flip and len(self.cards)>0:
                self.cards[0].flip()
            return nextCard
        else:
            return None

    def drawCard(self):
        if len(self.cards)>0:
            self.cards[0].flip()
            self.cards.append(self.cards.pop(0))
            self.cards[0].flip()
