# Lancer le serveur web :
uvicorn main:app --reload

## Récupérer un deck complet :
    http://127.0.0.1:8000/newDeck

## Récupérer le deck de chaque joueur :
    http://127.0.0.1:8000/dealCards/{nombre_de_joueurs}