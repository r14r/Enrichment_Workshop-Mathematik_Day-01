# Python für Kids (4. Auflage) - Kapitel 10
# Funktionen mit Wert

# Autor: Gregor Lingl
# Datum: 10. 8. 2009

# Verschieden Beispiele für Funktionen
# aus Kapitel 10

def reihe(staebchen):
    haufen = staebchen // 5
    rest = staebchen % 5
    ergebnis = "IIIII " * haufen + "I" * rest
    return ergebnis

def nachfolger(spieler, anzahl):
    return (spieler + 1) % anzahl

def fak(n):
    f = 1
    for k in range(2, n+1):
        f = f * k
    return f

def tabelle(bereich, funktion):
    for n in bereich:
        print(n, funktion(n))

def square(x):
    return x * x


