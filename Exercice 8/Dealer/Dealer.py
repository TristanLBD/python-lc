from Deck import Deck

class Dealer:
    def __init__(self, numPlayers: int):
        if numPlayers <= 0:
            raise ValueError("Le nombre minimum de joueur doit être de 1")

        self.__deck = Deck()
        self.__deck.shuffle()
        self.__numPlayers = numPlayers

        if numPlayers > self.__deck.remainingCards():
            raise ValueError("Le nombre de joueurs ne peut pas dépasser le nombre de cartes disponibles.")

        self.__hands = {f"Joueur {i + 1}": [] for i in range(numPlayers)}
        self.__distributeCards()

    def __distributeCards(self):
        while self.__deck.remainingCards() >= self.__numPlayers:
            for player in self.__hands:
                if self.__deck.remainingCards() > 0:
                    self.__hands[player].append(self.__deck.drawCard())

    def getHands(self):
        return {
            player: [{"rank": card.rank, "suit": card.suit, "color": card.color} for card in hand]
            for player, hand in self.__hands.items()
        }
