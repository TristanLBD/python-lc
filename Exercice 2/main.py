import re, json, fileinput

def validateIP(ip: str) -> str:
    if ip is None:
        raise ValueError("L'adresse IP ne peut pas être nulle")
    
    try:
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        ipv6_pattern = re.compile(r'^([\da-fA-F]{1,4}:){1,7}[\da-fA-F]{1,4}$')
        
        # Validation pour IPv4
        if ipv4_pattern.match(ip):
            parts = ip.split('.')
            if any(int(part) < 0 or int(part) > 255 for part in parts):
                raise ValueError("Les parties de l'IP IPv4 doivent être entre 0 et 255.")
            return "IPv4"
        
        # Validation pour IPv6
        if ipv6_pattern.match(ip):
            return "IPv6"
        
        # Si ce n'est ni IPv4 ni IPv6
        raise ValueError("Format d'adresse IP invalide")
    
    except ValueError as e:
        return f"Erreur: {e}"
    except re.error as e:
        return f"Erreur de regex: {e}"
    except TypeError as e:
        return f"Erreur: Type d'argument incorrect. {e}"
    except Exception as e:
        return f"Erreur inattendue: {e}"

def validateMultipleIPs(IPs: dict[str, str]) -> dict[str, dict[str, str]]:
    result = {}
    for host, ip in IPs.items():
        try:
            result[host] = {
                "IP": ip,
                "Version": validateIP(ip)
            }
        except ValueError as e:
            result[host] = {
                "IP": ip,
                "Version": f"Erreur de valeur: {e}"
            }
        except TypeError as e:
            result[host] = {
                "IP": ip,
                "Version": f"Erreur de type: {e}"
            }
        except re.error as e:
            result[host] = {
                "IP": ip,
                "Version": f"Erreur de regex: {e}"
            }
        except Exception as e:
            result[host] = {
                "IP": ip,
                "Version": f"Erreur inattendue: {e}"
            }
    return result

def replaceLettersInFile(filePath: str, letterToReplace: str = "a", letterUsed: str = "x"):
    try:
        # Lire et stocker tout le contenu du fichier
        with open(filePath, "r") as my_file:
            content = my_file.read()

        # Remplacer les lettres spécifiées par une autre
        new_content = content.replace(letterToReplace, letterUsed)

        # Ouvrir le fichiée pour y réecrire le contenu modifié
        with open(filePath, "w") as my_file:
            my_file.write(new_content) 
        print(f"Les lettres '{letterToReplace}' ont été remplacées par '{letterUsed}' dans le fichier.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filePath}' n'a pas été trouvé.")
    except PermissionError:
        print(f"Erreur : Permission refusée pour accéder au fichier '{filePath}'.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

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





try:
    replaceLettersInFile("./file.txt", letterToReplace="o")

    fileContentAsDictionnary = storeFileContentInDictionnary("file2.txt")
    print(fileContentAsDictionnary)

    for key, value in fileContentAsDictionnary.items():
        print(f"\nLigne numéro {key} : {len(value)} caractères  => {value}")

    userIP = input("Quelle est ton adresse IP ? ")
    print(f"Ton adresse IP est '{userIP}', elle est considérée comme {validateIP(userIP)}.")
    
    IPDictionnary = {
        "host1": "192.168.1.1",
        "host2": "2001:db8::ff00:42:8329",
        "host3": "999.999.999.999",
        "host4": "fe80::1ff:fe23:4567:890a",
        "host5": "256.256.256.256",
        "host6": False
    }

    print(json.dumps(validateMultipleIPs(IPDictionnary), indent=4, ensure_ascii=False))
except Exception as e:
    print(f"Une erreur s'est produite: {e}")
