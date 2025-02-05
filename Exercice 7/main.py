from fastapi import FastAPI, HTTPException
from Deck.Deck import Deck
from Dealer.Dealer import Dealer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI"}

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

    # if num_players < 2 or num_players > 10:
    #     raise HTTPException(status_code=400, detail="Le nombre de joueurs doit être compris entre 2 et 10.")

    # deck = Deck()
    # hands, remaining = deck.deal(num_players)
    # return {"hands": hands, "remaining": remaining}