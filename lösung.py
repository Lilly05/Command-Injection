import subprocess

def ping_host(ip_address):
    # Es wird eine Liste an die subprocess.run Methode übergeben
    command = ["ping", "-c", "4", ip_address]

    # shell=False ist der Default Wert. Dadurch wird die Benutzereingabe nicht mehr von der Shell interpretiert, sondern direkt als Liste von Befehlsargumenten behandelt.
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    user_input = input("Geben Sie die IP-Adresse ein, die Sie pingtesten möchten: ")

    # Zusätzlich wurde eine einfache Validierung implementiert, um sicherzustellen, dass die Benutzereingabe eine gültige IP-Adresse ist, um potenzielle Angriffe weiter zu erschweren.
    if not all(map(lambda x: x.isdigit() or x == '.', user_input)):
        print("Ungültige IP-Adresse!")
    else:
        print(ping_host(user_input))
