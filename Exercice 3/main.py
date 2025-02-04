import requests
import csv
import json


def executeAPIRequest(url: str, method: str = "GET", params: dict = None, data: dict = None) -> dict:
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
        return {"error": f"Erreur lors de la requête: {str(e)}"}

# Lire le fichier CSV et modifier son contenu
def modifyCSV(FIlePath: str, FinalFile: str):
    with open(FIlePath, mode="r", newline="", encoding="utf-8") as fichier_entree:
        lecteur_csv = csv.reader(fichier_entree)
        donnees = list(lecteur_csv)

        # Exemple de modification : ajouter une colonne "Modifié" avec une valeur
        if donnees:
            donnees[0].append("Modifié")  # Ajouter une en-tête
            for ligne in donnees[1:]:
                ligne.append("Oui")  # Ajouter une valeur pour chaque ligne

    # Sauvegarder les modifications dans un nouveau fichier
    with open(FinalFile, mode="w", newline="", encoding="utf-8") as fichier_sortie:
        ecrivain_csv = csv.writer(fichier_sortie)
        ecrivain_csv.writerows(donnees)

    print(f"Les données modifiées ont été enregistrées dans {FinalFile}.")

def storeFileContentInDictionnary(filePath: str) -> dict[int, str]:
    try:
        # Dictionnaire pour stocker le contenu du fichier
        dictionnaryContent = {}

        # Ouvrir le fichier en mode lecture
        with open(filePath, "r") as file:
            for lineNumber, lineContent in enumerate(file, start=1):  # start=1 pour que la numérotation commence à 1
                dictionnaryContent[lineNumber] = lineContent.strip()  # strip() sert a retirer les sauts de ligne

        return dictionnaryContent

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filePath}' n'a pas été trouvé.")
    except PermissionError:
        print(f"Erreur : Permission refusée pour accéder au fichier '{filePath}'.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def exportToJson(data: dict[int, str], outputFilePath: str):
    try:
        with open(outputFilePath, "w", encoding="utf-8") as jsonFile:
            for lineNumber, lineContent in data.items():
                json.dump({lineNumber: lineContent}, jsonFile, ensure_ascii=False)
                jsonFile.write("\n")
        print(f"Données exportées avec succès dans '{outputFilePath}'.")
    except Exception as e:
        print(f"Erreur lors de l'exportation JSON : {e}")

def exportToCsv(data: dict[int, str], outputFilePath: str):
    try:
        with open(outputFilePath, "w", newline="", encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["Ligne", "Contenu"])
            for lineNumber, lineContent in data.items():
                writer.writerow([lineNumber, lineContent])
        print(f"Données exportées avec succès dans '{outputFilePath}'.")
    except Exception as e:
        print(f"Erreur lors de l'exportation CSV : {e}")

# --------------------------------------------------------------- #

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
data = {"title": "foo", "body": "bar", "userId": 1}

# GET
getResult = executeAPIRequest(url, method="GET", params=params)
print(getResult)

# POST
# postResult = executeAPIRequest(url, method="POST", data=data)
# print(postResult)

# --------------------------------------------------------------- #

# modifyCSV("username.csv", "donnees_modifiees.csv")

# --------------------------------------------------------------- #

# fileData = storeFileContentInDictionnary("file.txt")
# exportToCsv(fileData, "fichier-cree.csv")

# --------------------------------------------------------------- #