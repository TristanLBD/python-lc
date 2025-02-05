from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./cardGame.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    num_players = Column(Integer, nullable=False)

class PlayerHand(Base):
    __tablename__ = "player_hands"
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    player_name = Column(String, nullable=False)
    cards = Column(String, nullable=False)
    game = relationship("Game", back_populates="hands")

Game.hands = relationship("PlayerHand", back_populates="game")

# Création des tables
Base.metadata.create_all(bind=engine)