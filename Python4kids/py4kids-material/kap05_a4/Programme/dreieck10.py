# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2008
# dreieck10.py:  3 gleichseitige farbige, gefüllte Dreiecke

from turtle import *

def dreieck(seite):
    """Zeichne Dreieck mit Seitenlänge seite.
    """
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    forward(seite)
    left(120)

def fuelle_dreieck(seitenlaenge):
    """Zeichne gefülltes Dreieck
    mit Seitenlänge seite.
    """
    begin_fill()
    dreieck(seitenlaenge)
    end_fill()
    
startseite = 65
aenderung = 35

reset()                        
pensize(10)                    
right(90)

seite = startseite

color("red", "cyan")
fuelle_dreieck(seite)

left(120)
seite = seite + aenderung

color("green", "magenta")
fuelle_dreieck(seite)

left(120)
seite = seite + aenderung

color("blue", "yellow")
fuelle_dreieck(seite)

left(120)
hideturtle()
