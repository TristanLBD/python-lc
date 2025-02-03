import re, json

def validateIP(ip: str) -> str:
    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ipv6_pattern = re.compile(r'^([\da-fA-F]{1,4}:){1,7}[\da-fA-F]{1,4}$')
    
    if ipv4_pattern.match(ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"
    
    if ipv6_pattern.match(ip):
        return "IPv6"
    
    return "IP invalide"

def validateIPDict(IPs):
    result = {}
    for host, ip in IPs.items():
        result[host] = {
            "IP": ip,
            "Version": validateIP(ip)
        }
    return result

userIP = input("Quelle est ton adresse IP ? ")
print(f"Ton adresse IP est '{userIP}', elle est considérée comme {validateIP(userIP)}.")

dictionnaireIP = {
    "host1": "192.168.1.1",
    "host2": "2001:db8::ff00:42:8329",
    "host3": "999.999.999.999",
    "host4": "fe80::1ff:fe23:4567:890a",
    "host5": "256.256.256.256"
}

print(json.dumps(validateIPDict(dictionnaireIP), indent=4, ensure_ascii=False))