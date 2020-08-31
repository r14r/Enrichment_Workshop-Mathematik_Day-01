# -*- coding: cp1252 -*-

# Python f�r Kids -- 3. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 18. 3. 2008
# dreieck08.py:  3 gleichseitige farbige, gef�llte Dreiecke
#                unterschiedlicher Gr��e, mit Funktion dreieck()
#                und Funktion fuelle_dreieck()

from xturtle import *

def dreieck():
    """Zeichne Dreieck mit Seitenl�nge seite.
    """
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    forward(seite)
    left(120)

def fuelle_dreieck():
    begin_fill()
    dreieck()
    end_fill()

startseite = 65
aenderung = 35

reset()            # leere Zeichenfl�che herstellen
pensize(10)        # Strichdicke 10 Pixel einstellen
right(90)          # turtle in Ausgangsrichtung drehen

seite = startseite

color("red", "cyan")
fuelle_dreieck()

left(120)
seite = seite + aenderung

color("green", "magenta")
fuelle_dreieck()

left(120)
seite = seite + aenderung

color("blue", "yellow")
fuelle_dreieck()

left(120)
hideturtle()
