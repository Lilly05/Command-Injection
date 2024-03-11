---
theme: gaia
_class: lead
backgroundColor: #E8E9F3
---
<style scoped>
  @import url('styles.css');
</style>

![bg left:40% 80%](https://iosec.in/wp-content/uploads/2018/01/command_injection-a0cfd67725c30fb75f4716b3cd123c76.png)

# Command Execution/ Injection

Lilly Koller

---

# Was ist Command Injection?

- Befehle können eingeschleust werden
- Anwendungen und Daten können kompromittiert werden
  - Kompromittiert: Daten wurden manipuliert und/ oder Systeme wurden von einer externen Quelle beeinflusst
- Angreifer können Zugriff oder Kontrolle für die Anwendung/ Server erhalten

---

# Wie funktioniert Command Injection?

- Meistens per Benutzereingabe
- Unsichere Daten werden übergeben
  - Formulare, Cookies, HTTP-Header u.s.w
- Keine/ Nicht genügend Eingabevalidierung
- Befehle werden mit den Berechtigungen der verwundbaren Anwendung ausgeführt

---

# Beispiel Command Injection

```python
import subprocess

def execute_command(command):
    subprocess.call(command, shell=True)

user_input = input("Gib bitte dein Name ein: ")

execute_command("echo " + "Hallo " + user_input)

```

---

# Beispiel ohne Command Injection

```python
import subprocess

def execute_command(command):
    subprocess.call(command)

user_input = input("Gib bitte deinen Namen ein: ")

execute_command(["echo", "Hallo " + user_input])

```

---
# Wie kann man das verhindern?

- Benutzereingabe client- und serverseitig validieren
  - Command Injection kommt vorallem vor, wenn nur clientseitig validiert wird
- Sonderzeichen aus Eingaben entfernen
- Code mit den niedrigsten Berechtigungen ausführen
- Bei z.B Dateinamen oder URLs validieren und unpassende Eingaben invalidieren