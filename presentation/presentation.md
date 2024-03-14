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
    - Meistens per Benutzereingabe
- Unsichere Daten werden übergeben
  - Formulare, Cookies, HTTP-Header u.s.w
- Befehle werden mit den Berechtigungen der verwundbaren Anwendung ausgeführt

---

# Mögliche Auswirkungen

- Datenmanipulation
    - Ausführung schädlicher Befehle (Löschen, Lesen, Bearbeiten) 
- unbefugten Zugriffs auf vertrauliche Informationen
- Angreifer können Kontrolle über das System übernehmen
- Rechte/ Privilegien verändern

---

# Beispiel Command Injection

```python
import subprocess

def ping_host(ip_address):
    command = "ping -c 4 " + ip_address
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    user_input = input("Geben Sie die IP-Adresse ein, die Sie pingen möchten: ")
    print(ping_host(user_input))
```

---

# Beispiel ohne Command Injection

```python
import subprocess

def ping_host(ip_address):
    command = ["ping", "-c", "4", ip_address]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    user_input = input("Geben Sie die IP-Adresse ein, die Sie pingtesten möchten: ")
    if not all(map(lambda x: x.isdigit() or x == '.', user_input)):
        print("Ungültige IP-Adresse!")
    else:
        print(ping_host(user_input))
```

