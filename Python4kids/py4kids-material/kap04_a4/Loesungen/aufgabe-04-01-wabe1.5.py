# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum 6. 8. 2009
# wabe1.5.py - Kapitel 4: Aufgabe 1
# Erster Lösungsschritt: Funktion sechseck() zeichnet sechs Sechsecke

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
left(120)
pendown()

pencolor("brown")
fillcolor("yellow")

begin_fill()
forward(55)
left(60)
forward(55)
left(60)
forward(55)
left(60)
forward(55)
left(60)
forward(55)
left(60)
forward(55)
left(60)
end_fill()

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
