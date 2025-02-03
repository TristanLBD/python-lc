import requests

def execute_api_request(url: str, method: str = "GET", params: dict = None, data: dict = None) -> dict:
    try:
        # Faire la requête GET ou POST en fonction de la méthode
        if method.upper() == "GET":
            response = requests.get(url, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, data=data)
        else:
            return {"error": "Méthode HTTP non supportée. Utilisez 'GET' ou 'POST'."}

        # Vérifier si la requête a réussi
        if response.status_code >= 400 and response.status_code < 500:
            return {"error": f"Erreur client {response.status_code}: {response.text}"}

        # Si la requête a réussi, retourner les données sous forme de dictionnaire
        try:
            return response.json()
        except ValueError:
            return {"error": "Réponse de l'API n'est pas au format JSON."}

    except requests.exceptions.RequestException as e:
        # Si une exception est levée (par exemple problème de connexion), retourner l'erreur
        return {"error": f"Erreur lors de la requête: {str(e)}"}

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
data = {"title": "foo", "body": "bar", "userId": 1}  # Données pour la requête POST

# GET
getResult = execute_api_request(url, method="GET", params=params)
print(getResult)

# POST
postResult = execute_api_request(url, method="POST", data=data)
print(postResult)