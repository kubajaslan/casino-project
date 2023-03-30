import random

suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')

ranks = ('Two',
         'Five',
         'Six',
         'Three',
         'Four',
         'Seven',
         'Eight',
         'Nine',
         'Ten',
         'Jack',
         'Queen',
         'King',
         'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self) -> str:
        deck_check = ''
        for card in self.deck:
            deck_check += '\n ' + card.__str__()
        return 'The deck you are using has: ' + deck_check

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)


