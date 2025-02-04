import re, json

def validateIP(ip: str) -> str:
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


def validateMultipleIPs(IPs: dict[str, str]) -> dict[str, dict[str, str]]:
    result = {}
    for host, ip in IPs.items():
        result[host] = {
            "IP": ip,
            "Version": validateIP(ip)
        }
    return result


def askUserForHisIP():
    userIP = input("Quelle est ton adresse IP ? ")
    print(f"Ton adresse IP est '{userIP}', elle est considérée comme {validateIP(userIP)}.")
# userIP = input("Quelle est ton adresse IP ? ")
# print(f"Ton adresse IP est '{userIP}', elle est considérée comme {validateIP(userIP)}.")

IPDictionnary = {
    "host1": "192.168.1.1",
    "host2": "2001:db8::ff00:42:8329",
    "host3": "999.999.999.999",
    "host4": "fe80::1ff:fe23:4567:890a",
    "host5": "256.256.256.256"
}

print(json.dumps(validateMultipleIPs(IPDictionnary), indent=4, ensure_ascii=False))