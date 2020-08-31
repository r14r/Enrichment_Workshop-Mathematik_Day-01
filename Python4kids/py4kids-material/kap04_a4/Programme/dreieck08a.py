# -*- coding: cp1252 -*-
# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# dreieck08a.py  --   !! Funktioniert NICHT !!

from turtle import *

def dreieck():
    """Zeichne Dreieck mit Seitenlänge seite.
    """
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    forward(seite)
    left(120)

def fuelle_dreieck():
    """Zeichne gefülltes Dreieck
    mit Seitenlänge seite.
    """
    begin_fill()
    dreieck()
    end_fill()
    seite = seite + aenderung
    left(120)  # Seite und Richtung 
               # fürs nächste Dreieck!

startseite = 65
aenderung = 35

reset()
pensize(10)
right(90)

seite = startseite

color("red", "cyan")
fuelle_dreieck()

color("green", "magenta")
fuelle_dreieck()

color("blue", "yellow")
fuelle_dreieck()

hideturtle()
