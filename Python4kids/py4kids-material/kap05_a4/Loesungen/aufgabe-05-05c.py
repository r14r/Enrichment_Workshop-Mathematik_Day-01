# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 08. 2009
# Loesung von Kapitel 5, Aufgabe 5(c): 

from turtle import *
from math import sqrt
from mytools import jump

SEITE = 125

def haus(seite):
    left(90)
    forward(seite)
    right(90)
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    forward(seite)
    left(75)
    forward(seite*sqrt(2))
    left(135)
    forward(seite)
    left(135)
    forward(seite*sqrt(2))
    left(135)
    forward(seite)


reset()
speed(1)
jump(SEITE*sqrt(3)/4, 180)
jump(SEITE*sqrt(2)/2, 225)
right(90)
pensize(3)

haus(SEITE)    

hideturtle()

