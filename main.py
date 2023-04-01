import random

suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')

ranks = ('Two',
         'Three',
         'Four',
         'Five',
         'Six',
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
                self.deck.append(Card(suit, rank))

    def __str__(self) -> str:
        deck_check = ''
        for card in self.deck:
            deck_check += '\n ' + card.__str__()
        return 'The deck you are using has: ' + deck_check + '\n - which in total is ' + str(len(self.deck)) + ' cards.'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def show_hand(self):
        for card in self.cards:
            print(card)

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1


def take_bet(account):
    while True:
        try:
            account.bet = int(input("Place your bet! How many chips? "))
        except ValueError:
            print("Enter en integer!")

        else:
            if account.bet > account.total:
                print("Not enough chips left! You only have " + str(account.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to hit or stand? h or s?")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing = False

        else:
            print("try again")
            continue

        break


def show_partial_cards(player_hand, dealer_hand):
    print("\nDealer's hand:")
    print(" *** ")
    print('', dealer_hand.cards[1])
    print("\nPlayer's hand:", *player_hand.cards, sep='\n ')


def show_all_cards(player_hand, dealer_hand):
    print("\nDealer's hand:", *dealer_hand.cards, sep='\n ')
    print("\nDealer's value:", dealer_hand.value)
    print("\nPlayer's hand:", *player_hand.cards, sep='\n ')
    print("\nPlayer's value:", player_hand.value)


def player_busts(player, dealer, chips):
    print("player busts!")
    chips.lose_bet()


def dealer_busts(player, dealer, chips):
    print("dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("dealer wins")
    chips.lose_bet()


def player_wins(chips):
    print("player wins")
    chips.win_bet()


class ChipAccount:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


playing = True
player_account = ChipAccount()

while True:
    print("Welcome to 21! Game started!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_account)

    show_partial_cards(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_all_cards(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_account)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all_cards(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_account)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_account)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_account)
        else:
            print("it's a tie!")

    print("player's winnings stand at: ", player_account.total)

    new_game = input("would u like to play another hand? y / n ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("thanks for playing")
        break
