# Write your blackjack game here.
# C - card
# R - value, suit, rank, know where it is in deck
# C - Deck
SUITS = ['♥️', '♦️', '♣️', '♠️']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# C - deck
# R - is shuffled, card dealt from it, holds the cards in an order,
# C - Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                if card.rank == 'A':
                    card.value = (1, 11)
                elif card.rank in range(2, 11):
                    card.value = rank
                else:
                    card.value = 10

                print(card)
                self.cards.append(card)
        print(f'There are {len(self.cards)} in this deck.')


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        super().__init__('Dealer')


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(name=input("What is your name? "))
        self.dealer = Dealer()

# ace_of_spades = Card(suit='♠️', rank='A', value=(1, 11))
# four_of_clubs = Card(suit='♣️', rank=4, value=4)


# print(ace_of_spades)
# print(four_of_clubs)

new_game = Game()
breakpoint()