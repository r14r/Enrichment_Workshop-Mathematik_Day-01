# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# dreieck13.py:  zeichnet drei unterschiedliche Dreierpacks
#                von Dreiecken

from turtle import *

def jump(distanz, winkel):
    """springt um eine Strecke der Länge distanz
    in die Richtung von winkel"""
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

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
right(90)

jump(123, -135)
pensize(3)
left(15)
dreierpack(35,10)

jump(200, 30)
pensize(5)
right(60)
dreierpack(75, -15)

jump(240, 110)
pensize(7)
left(150)
dreierpack(30, 35)

hideturtle()
