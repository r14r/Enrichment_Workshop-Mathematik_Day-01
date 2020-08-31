# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 08. 2009
# Loesung von Kapitel 5, Aufgabe 5(a): 

from turtle import *
from math import sqrt

def dreieck45(seite):
    forward(seite)
    left(135)
    forward(seite*sqrt(2))
    left(135)
    forward(seite)
    left(90)

reset()         
dreieck45(100)


