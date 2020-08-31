# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# dreierpack.py:     Dreierpacks von Dreiecken:
#                3 gleichseitige farbige, gefüllte Dreiecke
# unterschiedlicher Größe, mit Funktion dreieck() MIT EINEM
# PARAMETER und Funktion fuelle_dreieck() MIT DREI PARAMETERN!

from turtle import *

def dreieck(laenge):
    """zeichne Dreieck mit Seitenlänge laenge.
    """
    for i in range(3):
        forward(laenge)
        left(120)

def fuelle_dreieck(seitenlaenge, stiftfarbe, fuellfarbe):
    """Zeichne gefülltes Dreieck mit Seitenlänge seitenlaenge.
    """
    color(stiftfarbe, fuellfarbe)
    begin_fill()
    dreieck(seitenlaenge)
    end_fill()

def dreierpack(seite, aenderung, farbpaare):
    """Zeichne Muster aus drei Dreiecken.
    1. Dreieck hat Seitenlänge startseite.
    """
    for farbpaar in farbpaare:
        stiftfarbe, fuellfarbe = farbpaar
        fuelle_dreieck(seite, stiftfarbe, fuellfarbe)
        left(120)
        seite = seite + aenderung
    

reset()
pensize(10)
right(90)
farbenpaare = (("red","cyan"), ("green","magenta"),
               ("blue","yellow"))
dreierpack(65, 35, farbenpaare)
hideturtle()
