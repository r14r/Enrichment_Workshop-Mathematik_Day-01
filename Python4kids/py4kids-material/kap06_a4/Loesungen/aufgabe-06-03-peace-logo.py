# Python für Kids -- 4. Auflage, 2009
# Autor: Gregor Lingl
# Datum : 11. 10. 2009
# myfigures.py
# peace_logo.py : Kapitel 6, Aufgabe 2 : Friedenszeichen

from turtle import *

GRAU = (0.3, 0.3, 0.3)         # Siehe Kapitel 8, Seite 224
LILA = (1, 0.2, 0.8)
VIOLETT = (0.8, 0.4, 0.8)
GELB = (1, 1, 0.2)
HELLGRUEN = (0.8, 1, 0.8)
ROT = (0.8, 0, 0)
BLAU = (0, 0.4, 1)
GRUEN = (0.4, 0.8, 0.4)
CREME = (1, 0.8, 0.4)

def quadrat(seite, fuellfarbe):
    fillcolor(fuellfarbe)
    begin_fill()
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)
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

def peace_logo():
    pencolor(GRAU)
    # Vier Quadrate
    pensize(15)
    quadrat(120, LILA)
    right(90)
    quadrat(120, VIOLETT)
    right(90)
    quadrat(120, GELB)
    right(90)
    quadrat(120, HELLGRUEN)
    right(90)
    # Vier Sektoren
    pensize(10)
    sektor(109, 135, CREME)    
    left(135)
    sektor(109, 45, GRUEN)    
    left(45)
    sektor(109, 45, BLAU)    
    left(45)
    sektor(109, 135, ROT)    
    left(135)
    
reset()
peace_logo()
hideturtle()



