# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum: 9. 8. 2009
# radioaktiv.py : Kapitel 8, Aufgabe 1 : Radioaktivitäts-Warnzeichen

from turtle import *
from mytools import jump
from math import sqrt

def quadrat(seite, fuellfarbe):
    fillcolor(fuellfarbe)
    begin_fill()
    for i in range(4):
        forward(seite)
        left(90)
    end_fill()

def sektor(radius, winkel, fuellfarbe):
    fillcolor(fuellfarbe)
    begin_fill()
    forward(radius)
    left(90)
    circle(radius,winkel)
    left(90)
    forward(radius)
    left(180-winkel)
    end_fill()

def kreis(radius, randfarbe, fuellfarbe):
    penup()
    color(randfarbe, fuellfarbe)
    forward(radius)
    left(90)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    
def radioaktiv(seite):    
    # zum Startpunkt
    jump(seite/sqrt(2), 135)  # Im Quadrat: Diagonale = Seite * (Wurzel aus 2)
    # Quadrat zeichnen
    quadrat(seite, "yellow")
    # zurück zum Ursprung zurück und nach rechts drehen
    jump(seite/sqrt(2), -45)
    right(90)
    # drei schwarze Sektoren zeichnen
    for i in range(3):
        sektor(seite*0.4, 60, "black")
        left(120)
    # Zentraler Kreis
    kreis(seite/8.0, "yellow", "black")


reset()
pensize(5)
radioaktiv(260)
hideturtle()



