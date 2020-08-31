# Python für Kids -- 4. Auflage, Kapitel 10
# Funktionen mit Wert

# Autor: Gregor Lingl
# Datum: 10. 8. 2009

# fak01.py  -  Die Faktorielle-Funktion


def fak(n):
    f = 1
    for k in range(2, n+1):
        f = f * k
    return f

def tabelle(bereich, funktion):
    for n in bereich:
        print(n, funktion(n))

tabelle(range(1,21), fak)


