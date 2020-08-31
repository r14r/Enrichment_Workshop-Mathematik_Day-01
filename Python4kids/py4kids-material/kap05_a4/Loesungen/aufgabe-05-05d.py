# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 08. 2009
# Loesung von Kapitel 5, Aufgabe 5(d): 

from turtle import *
from math import sqrt

# Falls du hopp noch nicht in deine eigene Python-Bibiliothek
# gestellt hast, hier eine vereinfachte Version: hopp()

def hopp(laenge):
    up()
    forward(laenge)
    down()

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
right(90)
hopp(-120)
haus(60)
hopp(15)
haus(45)
hopp(10)
haus(35)
hideturtle()


