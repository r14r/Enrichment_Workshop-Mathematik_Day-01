# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# Lösung von Kapitel 5, Aufgabe 1
# Zeichne ist eine Funktion, die wahlweise
# ein Quadrat oder ein Rechteck zeichnet

from turtle import *

def zeichne(figur, laenge):
    if figur == "quadrat":
        winkel = 90
    elif figur == "dreieck":
        winkel = 120
    forward(laenge)
    left(winkel)
    forward(laenge)
    left(winkel)
    forward(laenge)
    left(winkel)
    if figur == "quadrat":
        forward(laenge)
        left(winkel)

# wir probieren zeichne() aus:

reset()
right(90)
pensize(5)
color("blue")
zeichne("quadrat",50)
penup()
forward(75)
pendown()
color("green", "red")
begin_fill()
zeichne("dreieck", 70)
penup()
end_fill()


