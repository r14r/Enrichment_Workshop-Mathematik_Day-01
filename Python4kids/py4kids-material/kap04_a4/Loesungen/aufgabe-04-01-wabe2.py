# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum 6. 8. 2009
# wabe2.py - Kapitel 4: Aufgabe 1 
# Funktion sechseck() zeichnet sechs Sechsecke
# und vorher noch das innere Sechseck

from turtle import *

def sechseck():
    begin_fill()
    forward(55)
    right(60)
    forward(55)
    right(60)
    forward(55)
    right(60)
    forward(55)
    right(60)
    forward(55)
    right(60)
    forward(55)
    right(60)
    end_fill()
    
reset()

penup()
right(120)
forward(55)
## !!! Änderung !!!
right(120)  # hier
pendown()   

pencolor("brown")
fillcolor("yellow")
sechseck()  # und hier
right(120)  # und hier !!
## !!!

fillcolor("orange")

sechseck()
penup()
forward(55)
left(60)
pendown()

sechseck()
penup()
forward(55)
left(60)
pendown()

sechseck()
penup()
forward(55)
left(60)
pendown()

sechseck()
penup()
forward(55)
left(60)
pendown()

sechseck()
penup()
forward(55)
left(60)
pendown()

sechseck()
hideturtle()
