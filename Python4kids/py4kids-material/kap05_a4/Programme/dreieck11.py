# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2008
# dreieck11.py:  3 gleichseitige farbige, gefüllte Dreiecke

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

def fuelle_dreieck(seitenlaenge, stiftfarbe, fuellfarbe):
    """Zeichne gefülltes Dreieck
    mit Seitenlänge seite.
    """
    color(stiftfarbe, fuellfarbe)
    begin_fill()
    dreieck(seitenlaenge)
    end_fill()
    
startseite = 65
aenderung = 35

reset()                        
pensize(10)                    
right(90)

seite = startseite
fuelle_dreieck(seite, "red", "cyan")

left(120)
seite = seite + aenderung
fuelle_dreieck(seite, "green", "magenta")

left(120)
seite = seite + aenderung
fuelle_dreieck(seite, "blue", "yellow")

left(120)
hideturtle()
