# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2008
# dreieck08.py:  3 gleichseitige farbige, gefüllte Dreiecke

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
    mir Seitenlänge seite.
    """
    begin_fill()
    dreieck()
    end_fill()
    
startseite = 65
aenderung = 35

reset()                        
pensize(10)                    
right(90)

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
