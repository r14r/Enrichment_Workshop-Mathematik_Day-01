# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# dreieck14.py
# Verwendung von 'Schleifen, die zählen': for-Schleifen

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
for farbe in ("pink", "blue", "green"):
    dreieck(seite, farbe)
    left(120)
    seite = seite - 20

hideturtle()
