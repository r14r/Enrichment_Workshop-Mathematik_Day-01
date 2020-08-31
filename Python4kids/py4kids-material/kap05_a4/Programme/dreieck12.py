# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2008
# dreieck12.py:  Dreierpacks von Dreiecken:
# 3 gleichseitige farbige, gefüllte Dreiecke unterschiedlicher Größe,
# mit Funktion dreieck() MIT EINEM PARAMETER
# und Funktion fuelle_dreieck() MIT DREI PARAMETERN!

from turtle import *

def dreieck(laenge):
    """zeichne Dreieck mit Seitenlänge laenge.
    """
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)

def fuelle_dreieck(seitenlaenge, stiftfarbe, fuellfarbe):
    """Zeichne gefülltes Dreieck mit Seitenlänge seitenlaenge.
    """
    color(stiftfarbe, fuellfarbe)
    begin_fill()
    dreieck(seitenlaenge)
    end_fill()

def dreierpack(startseite, aenderung):
    """Zeichne Muster aus drei Dreiecken.
    1. Dreieck hat Seitenlänge startseite.
    """
    seite = startseite
    fuelle_dreieck(seite, "red", "cyan")

    left(120)
    seite = seite + aenderung
    fuelle_dreieck(seite, "green", "magenta")
    
    left(120)
    seite = seite + aenderung
    fuelle_dreieck(seite, "blue", "yellow")

    left(120)

reset()
pensize(10)
right(90)
dreierpack(65, 35)
hideturtle()
