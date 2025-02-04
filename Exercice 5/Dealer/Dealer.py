from Deck import Deck

class Dealer:
    def __init__(self, numPlayers: int):
        if numPlayers <= 0:
            raise ValueError("Le nombre minimum de joueur doit etre de 1")
        
        self.__deck = Deck()
        self.__deck.shuffle()
        self.__numPlayers = numPlayers

        # Vérification du nombre de joueurs par rapport au nombre de cartes
        if numPlayers > self.__deck.size():
            raise ValueError("Le nombre de joueurs ne peut pas dépasser le nombre de cartes disponibles.")

        self.__hands = {}
        for i in range(numPlayers):
            player_name = f"Joueur {i + 1}"
            self.__hands[player_name] = []

        self.__distributeCards()

    def __distributeCards(self):
        while self.__deck.remainingCards() >= self.__numPlayers:
            for player in self.__hands:
                if self.__deck.remainingCards() > 0:
                    self.__hands[player].append(self.__deck.drawCard())
        
    def getHands(self):
        return self.__hands

    def __str__(self):
        message = ""
        for player, hand in self.__hands.items():
            hand_str = []
            for card in hand:
                hand_str.append(str(card))
            PlaterNumCards = len(hand)
            message += f"{player} ({PlaterNumCards} cartes): {', '.join(hand_str)}\n\n"
        return message.strip()