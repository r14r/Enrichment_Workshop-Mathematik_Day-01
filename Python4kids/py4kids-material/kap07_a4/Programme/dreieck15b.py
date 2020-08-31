# Python für Kids -- 4. Auflage, Kapitel 7

# Autor: Gregor Lingl
# Datum: 8. 8. 2009
# dreieck15b.py  --  Weiterentwicklung von dreieck15.py
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
pensize(7)
speed(0)

seite = 20.0
farben = ("red", "blue", "green", "orange", "pink") * 10
# was ist nun der Wert von Farben?
anzahl = len(farben)
aenderung = (140 - seite) / anzahl
tracer(False) # stellt die Animation ab
for farbe in farben:
    dreieck(seite, farbe)
    left(360 / anzahl)
    seite = seite + aenderung
    update()  # bringt Grafik auf den aktuellen Stand

hideturtle()
tracer(True)  # stellt die Animation wieder an

