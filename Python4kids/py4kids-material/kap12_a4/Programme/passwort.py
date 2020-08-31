# Python für Kids (4. Auflage) - Kapitel 12
# Wörterbücher, Dateien ...

# Autor: Gregor Lingl
# Datum: 12. 8. 2009

# passwort.py  

passwort = { "griemer" : "elli007",
             "kkrahl"  : "Susim1",
             "kschrei" : "gottogott"
           }

def login():
    while True:  # endlose Anmeldeprozedur
        name = input("Username: ")
        pwd = input("Password: ")
        if (name, pwd) in passwort.items():
            print("Hi, {0}! Have fun!".format(name[1:]))
            break
        print("Anmeldung misslungen!")

        
