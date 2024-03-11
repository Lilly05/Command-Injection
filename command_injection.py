import subprocess

# Durch shell=True ist man anfälliger für Command Injection
# Die Befehle werden in einer neuen Shell-Prozessinstanz ausgeführt, was bedeutet, dass die Eingabe möglicherweise als Shell-Befehl interpretiert wird
def execute_command(command):
    subprocess.call(command, shell=True)

user_input = input("Gib bitte dein Name ein: ")

execute_command("echo " + "Hallo " + user_input)
