import subprocess

def ping_host(ip_address):
    # Ein einzelner String wird an die subprocess.run Methode mitgegeben
    command = "ping -c 4 " + ip_address

    # shell=True bedeutet, dass die Benutzereingabe direkt von der Shell interpretiert wird, ohne dass sie vorher sicher behandelt wird.
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    user_input = input("Geben Sie die IP-Adresse ein, die Sie pingen möchten: ")
    print(ping_host(user_input))