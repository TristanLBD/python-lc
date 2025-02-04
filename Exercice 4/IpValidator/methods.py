import re

class IPValidator:
    def __init__(self):
        pass

    def validateIP(self, ip: str) -> str:
        """
        Valide si une adresse IP est IPv4 ou IPv6.
        
        :param ip: L'adresse IP sous forme de chaîne.
        :return: "IPv4" si l'adresse est une IPv4, "IPv6" si l'adresse est une IPv6, "IP invalide" sinon.
        """
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        ipv6_pattern = re.compile(r'^([\da-fA-F]{1,4}:){1,7}[\da-fA-F]{1,4}$')

        # Validation pour IPv4
        if ipv4_pattern.match(ip):
            parts = ip.split('.')
            if all(0 <= int(part) <= 255 for part in parts):
                return "IPv4"
        
        # Validation pour IPv6
        if ipv6_pattern.match(ip):
            return "IPv6"
        
        # Si ce n'est ni IPv4 ni IPv6
        return "IP invalide"

    def askUserForHisIP(self):
        """
        Demande à l'utilisateur de saisir son adresse IP, puis affiche sa validation.
        """
        userIP = input("Quelle est ton adresse IP ? ")
        print(f"Ton adresse IP est '{userIP}', elle est considérée comme {self.validateIP(userIP)}.")
