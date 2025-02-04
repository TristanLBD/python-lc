class PlayingCard:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["Coeur", "Diamant", "Trefle", "Pique"]

    def __init__(self, rank: str, suit: str):
        if rank not in self.RANKS:
            raise ValueError(f"Numéro de carte invalide : {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Type de carte invalide : {suit}")
        
        self.__rank = rank  # Private attribute
        self.__suit = suit  # Private attribute
    
    def __str__(self):
        return f"{self.__rank} de {self.__suit}"

    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        return self.__suit
