# Python für Kids -- 4. Auflage, Kapitel 5

# Autor: Gregor Lingl
# Datum: 6. 8. 2009

# mytools.py : Meine Bibliothek von selbst erstellten 
# brauchbaren Funktionen für die Arbeit mit Python für Kids.

from turtle import *

def jump(distanz, winkel=0):
    """springt um eine Strecke der Länge distanz
    in die Richtung von winkel"""
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def strichel(laenge, striche=10):
    spruenge = striche - 1
    strich = laenge / (striche + spruenge)
    for i in range(spruenge):
        forward(strich)
        jump(strich)
    forward(strich)

def krange(start, stop, schritt=1):
    """erzeugt Liste von floating point Zahlen
    von start bis stop mit Schrittweite step."""
    zahlenliste = []
    element = float(start)  # macht aus start ein Kommazahl
    while element < stop:
        zahlenliste.append(element)
        element = element + schritt
    return zahlenliste

def frange(start, stop, schritt=1):
    """ein Generator von floating point Zahlen
    von start bis stop mit Schrittweite step."""
    element = float(start)  # macht aus start ein Kommazahl
    while element < stop:
        yield element
        element = element + schritt


