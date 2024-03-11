import subprocess

# shell=False ist der Standartwert. 
# Der Befehl wird direkt als ausführbares Programm behandelt, ohne von der Shell interpretiert zu werden
def execute_command(command):
    subprocess.call(command)

user_input = input("Gib bitte deinen Namen ein: ")

# Die beiden Textketten werden miteinander kombiniert. Es wird als Liste übergeben, damit nicht der ganze String von der Shell interpretiert wird
execute_command(["echo", "Hallo " + user_input])
