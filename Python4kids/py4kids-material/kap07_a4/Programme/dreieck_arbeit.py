# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# dreieck15.py
# Zum Einstieg in 'Schleifen, die zählen'.
from turtle import *

def dreieck(laenge, farbe):
    """Zeichne Dreieck mit Seitenlänge laenge.
    Dreieckseiten werden in farbe gezeichnet.
    """
    pencolor(farbe)
    for i in range(3):
        forward(laenge)
        left(120)

reset()
pensize(10)
seite = 100
farben = ("red", "blue", "green", "orange", "pink")
anzahl = len(farben)
for farbe in farben:
    dreieck(seite, farbe)
    left(360 / anzahl)
    seite = seite - 20

hideturtle()
