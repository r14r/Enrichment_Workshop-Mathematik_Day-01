# Python für Kids -- 4. Auflage, 2009
# Autor: Gregor Lingl
# Datum : 6. 8. 2009
# myfigures.py
# Python für Kids, Kapitel 6, Aufgabe 1

from turtle import *
from math import sqrt

def rechteck(laenge, breite):
    penup()
    forward(breite/2.0)
    left(90)
    forward(laenge/2.0)
    left(90)
    pendown()
    forward(breite)
    left(90)
    forward(laenge)
    left(90)
    forward(breite)
    left(90)
    forward(laenge)
    left(90)
    penup()
    forward(breite/2.0)
    left(90)
    forward(laenge/2.0)
    left(90)

def quadrat(laenge):
    rechteck(laenge, laenge)

def dreieck(seite):
    penup()
    h = sqrt(3)*seite/2
    forward(2.0*h/3.0)
    pendown()
    left(150)
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    left(30)
    penup()
    forward(2.0*h/3.0)
    left(180)    

def kreis(radius):
    penup()
    forward(radius)
    left(90)
    pendown()
    circle(radius)
    penup()
    right(90)
    back(radius)
    
def sektor(radius, winkel):
    pendown()
    right(winkel/2.0)
    forward(radius)
    left(90)
    circle(radius, winkel)
    left(90)
    forward(radius)
    left(180-winkel/2.0)
    penup()
    

if __name__ == "__main__":
    # Test und Demo.
    reset()
    rechteck(320,240)
    quadrat(200)
    dreieck(150)
    kreis(25*sqrt(3))
    sektor(35, 120)
    back(25)
