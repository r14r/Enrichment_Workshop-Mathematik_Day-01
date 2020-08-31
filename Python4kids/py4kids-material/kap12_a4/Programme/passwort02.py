# Python für Kids (4. Auflage) - Kapitel 12
# Wörterbücher, Dateien ...

# Autor: Gregor Lingl
# Datum: 12. 8. 2009

# passwort02.py  

passwort = {"griemer" : "elli007",
            "kkrahl"  : "susim1",
            "kschrei" : "gottogott"
           }

def login():
    versuche = 0
    while True:  # Anmeldeprozedur mit maximal 3 Versuchen
        versuche = versuche + 1
        name = input("Username: ")
        pwd = input("Password: ")
        if name in passwort:
            if pwd == passwort[name]:
                print("Hi, {0}! Have fun!".format(name[1:]))
                break
        print("Anmeldung misslungen!")
        if versuche == 3:
            print("ENDE! - Das hier ist ja keine Lotterie!")
            break

if __name__ == "__main__":
    login()
