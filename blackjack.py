import random

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
                    card.value = (11)
                elif card.rank in range(2, 11):
                    card.value = rank
                else:
                    card.value = 10

                print(card)
                self.cards.append(card)
        print(f'There are {len(self.cards)} in this deck.')

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def look_at_hand(self):
        '''Shows cards in hand to player'''
        for card in self.hand:
            print(f'The player\'s card is {card}')

    def if_ace(self, card, value):
        '''Change value of Ace to 1 if total value exceeds 21'''
        for card in self.hand:
            if card.rank == "A" and value > 21:
                value -= 10
        return value

    def calculate_hand_value(self):
        '''return the total value of the hand'''
        total_value = 0
        for card in self.hand:
            total_value += card.value
        total_value = self.if_ace(card, total_value)
        print(total_value)


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        super().__init__('Dealer')

    def look_at_top_card(self):
        print(f'The dealer\'s top card is {self.hand[0]}')


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(name=input("What is your name? "))
        self.dealer = Dealer()
        self.deal_cards()

# ace_of_spades = Card(suit='♠️', rank='A', value=(1, 11))
# four_of_clubs = Card(suit='♣️', rank=4, value=4)
    def deal_cards(self):
        '''Deal 2 cards each to the player and the dealer '''
        while len(self.player.hand) < 2 and len(self.dealer.hand) < 2:
            card = self.deck.cards.pop()
            self.player.hand.append(card)
            card = self.deck.cards.pop()
            self.dealer.hand.append(card)
        print(f'{self.player} has {self.player.hand} \n'
              f'and {self.dealer} has {self.dealer.hand}')

    def hit(self, player):
        '''Deal one card to the selected player'''
        card = self.deck.cards.pop()
        self.player.hand.append(card)

# print(ace_of_spades)
# print(four_of_clubs)


new_game = Game()
new_game.hit(new_game.player)
new_game.player.look_at_hand()
# Player.calculate_hand_value(new_game)
breakpoint()
# TODO Add values of each hand so player and dealer can decide to hit or stay