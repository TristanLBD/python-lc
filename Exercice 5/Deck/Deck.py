import random
from PlayingCard import PlayingCard

class Deck:
    def __init__(self):
        self.__cards = []
        for suit in PlayingCard.SUITS:
            for rank in PlayingCard.RANKS:
                card = PlayingCard(rank, suit)
                self.__cards.append(card)

    def shuffle(self):
        random.shuffle(self.__cards)

    def drawCard(self):
        if not self.__cards:
            raise IndexError("Impossible de piocher dans un deck vide.")
        return self.__cards.pop()

    def remainingCards(self):
        return len(self.__cards)
    
    def size(self):
        return len(self.__cards)
    
    def __str__(self):
        message = f"Le paquet contient {len(self.__cards)} cartes:\n"
        for card in self.__cards:
            message += str(card) + "\n"
        return message