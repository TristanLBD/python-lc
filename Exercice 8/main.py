from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Game, PlayerHand
from Deck import Deck
from Dealer import Dealer

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "FastAPI est en fonctionnement"}

@app.get("/newDeck")
def get_deck():
    deck = Deck()
    deck.shuffle()
    return {"deck": [str(card) for card in deck._Deck__cards]}

@app.post("/dealCards/{player_number}")
def deal_cards(player_number: int, db: Session = Depends(get_db)):
    if player_number <= 0:
        raise HTTPException(status_code=400, detail="Le nombre minimum de joueurs doit être 1.")

    dealer = Dealer(player_number)
    hands = dealer.getHands()

    # Création d'une nouvelle partie en base de données
    new_game = Game(num_players=player_number)
    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    # Stockage du deck de chaque joueur
    for player, hand in hands.items():
        cards_str = ", ".join(str(card) for card in hand)
        player_hand = PlayerHand(game_id=new_game.id, player_name=player, cards=cards_str)
        db.add(player_hand)

    db.commit()
    
    return {"game_id": new_game.id, "hands": hands}

@app.get("/game/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Partie non trouvée.")

    players = db.query(PlayerHand).filter(PlayerHand.game_id == game_id).all()
    hands = {player.player_name: player.cards for player in players}

    return {"game_id": game.id, "num_players": game.num_players, "hands": hands}
