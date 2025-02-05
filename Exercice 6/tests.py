import unittest
from Deck import Deck
from PlayingCard import PlayingCard
from Dealer import Dealer

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    # Tester que le mélange modifie bien l'ordre des cartes.
    def test_shuffle(self):
        initial_order = self.deck._Deck__cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(initial_order, self.deck._Deck__cards, "Le paquet devrait être mélangé.")
    
    # Vérifier que piocher une carte réduit bien la taille du deck
    def test_draw_card(self):
        initial_size = self.deck.remainingCards()
        drawn_card = self.deck.drawCard()
        self.assertIsInstance(drawn_card, PlayingCard, "L'objet retourné devrait être une carte.")
        self.assertEqual(self.deck.remainingCards(), initial_size - 1, "La taille du deck devrait diminuer de 1.")
    
    # Vérier qu'il est impossible de piocher dans un deck vide
    def test_draw_card_empty_deck(self):
        for _ in range(52):
            self.deck.drawCard()
        with self.assertRaises(IndexError):
            self.deck.drawCard()

    # Verifier que le nombre de carte est cohérent apres chaque action effectuée sur le deck
    def test_remaining_cards(self):
        self.assertEqual(self.deck.remainingCards(), 52, "Un deck neuf devrait contenir 52 cartes.")
        self.deck.drawCard()
        self.assertEqual(self.deck.remainingCards(), 51, "Après une pioche, il devrait rester 51 cartes.")
    
    def test_size(self):
        self.assertEqual(self.deck.size(), 52, "Un deck neuf devrait contenir 52 cartes.")
        self.deck.drawCard()
        self.assertEqual(self.deck.size(), 51, "Après une pioche, il devrait rester 51 cartes.")
        
class TestPlayingCard(unittest.TestCase):
    # Test de création d'une carte valide
    def test_valid_card(self):
        card = PlayingCard("A", "Coeur")
        self.assertEqual(card.rank, "A", "Le rang de la carte devrait être 'A'.")
        self.assertEqual(card.suit, "Coeur", "La couleur de la carte devrait être 'Coeur'.")

    # Test de création d'une carte invalide
    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            PlayingCard("X", "Coeur")
    
    # Test de création avec une famille invalide
    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard("A", "Etoile")


class TestDealer(unittest.TestCase):
    # Verifier que le nombre de joueurs gérés par le dealer est le meme que celui renseigné par le joueur
    def test_valid_initialization(self):
        dealer = Dealer(4)
        self.assertEqual(len(dealer.getHands()), 4, "Le nombre de mains distribuées doit être égal au nombre de joueurs.")
    
    # Tester qu'une erreur est renvoyée lorsque le nbr de joueur est invalide (0 ou supérieur au nbr de cartes)
    def test_invalid_num_players(self):
        with self.assertRaises(ValueError):
            Dealer(0)
        with self.assertRaises(ValueError):
            Dealer(53)
    
    # Tester que les cartes sont réparties équitablement
    def test_card_distribution(self):
        dealer = Dealer(4)
        hands = dealer.getHands()
        num_cards = [len(hand) for hand in hands.values()]
        self.assertTrue(all(x == num_cards[0] for x in num_cards), "Tous les joueurs devraient avoir le même nombre de cartes ou presque.")

if __name__ == '__main__':
    unittest.main()
