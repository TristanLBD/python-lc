from fastapi import FastAPI, HTTPException
from Deck import Deck
from Dealer import Dealer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI est en fonctionnement"}

@app.get("/newDeck")
def get_deck():
    deck = Deck()
    deck.shuffle()
    cards_list = []
    for card in deck._Deck__cards:
        cards_list.append(str(card))
    return {"deck": cards_list}

@app.get("/dealCards/{player_number}")
def deal_cards(player_number: int):
    dealer = Dealer(player_number)
    hands = dealer.getHands()
    return {"hands": hands}