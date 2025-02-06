import random
from PlayingCard import PlayingCard

class Deck:
    def __init__(self):
        self.__cards = [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]

    def shuffle(self):
        random.shuffle(self.__cards)

    def drawCard(self):
        if not self.__cards:
            raise IndexError("Impossible de piocher dans un deck vide.")
        return self.__cards.pop()

    def remainingCards(self):
        return len(self.__cards)

    def __str__(self):
        return "\n".join(str(card) for card in self.__cards)

    def get_cards(self):
        return [{"rank": card.rank, "suit": card.suit, "color": card.color} for card in self.__cards]
