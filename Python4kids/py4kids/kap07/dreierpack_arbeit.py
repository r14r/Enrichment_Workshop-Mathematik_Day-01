# -*- coding: cp1252 -*-
# Python f�r Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 7. 8. 2008
# dreierpack_arbeit_.py:     Dreierpacks von Dreiecken:
#                3 gleichseitige farbige, gef�llte Dreiecke
# unterschiedlicher Gr��e, mit Funktion dreieck() MIT EINEM
# PARAMETER und Funktion fuelle_dreieck() MIT DREI PARAMETERN!

from turtle import *

def dreieck(laenge):
    """zeichne Dreieck mit Seitenl�nge laenge.
    """
    for i in range(3):
        forward(laenge)
        left(120)

def fuelle_dreieck(seitenlaenge, stiftfarbe, fuellfarbe):
    """Zeichne gef�lltes Dreieck mit Seitenl�nge seitenlaenge.
    """
    color(stiftfarbe, fuellfarbe)
    begin_fill()
    dreieck(seitenlaenge)
    end_fill()

def dreierpack(seite, aenderung):
    """Zeichne Muster aus drei Dreiecken.
    1. Dreieck hat Seitenl�nge startseite.
    """
    fuelle_dreieck(seite, "red", "cyan")
    left(120)
    seite = seite + aenderung
    
    fuelle_dreieck(seite, "green", "magenta")
    left(120)
    seite = seite + aenderung
    
    fuelle_dreieck(seite, "blue", "yellow")
    left(120)
    seite = seite + aenderung

reset()
pensize(10)
right(90)
dreierpack(65, 35)
hideturtle()
