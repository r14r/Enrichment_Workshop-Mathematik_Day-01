# Python für Kids -- 4. Auflage, Kapitel 7

# Autor: Gregor Lingl
# Datum: 8. 8. 2009
# dreieck15a.py  --  Weiterentwicklung von dreieck15.py
# wie im Buch angeführt: Variable aenderung eingeführt

# Als Anregung für weitere Experimente 

from turtle import *

def dreieck(laenge, farbe):
    """Zeichne Dreieck mit Seitenlänge laenge.
    Dreieckseiten werden in der Farbe farbe gezeichnet.
    """
    pencolor(farbe)
    for i in range(3):
        forward(laenge)
        left(120)

reset()
pensize(10)

seite = 145.0
farben = ("red", "blue", "green", "orange", "pink")
anzahl = len(farben)
aenderung = seite / anzahl
for farbe in farben:
    dreieck(seite, farbe)
    left(360 / anzahl)
    seite = seite - aenderung

hideturtle()

