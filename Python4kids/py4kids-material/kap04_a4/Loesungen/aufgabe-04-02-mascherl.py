# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# aufgabe-04-02.py  -  Kapitel 4, Aufgabe 2

from turtle import *

def dreieck():
    """zeichne Dreieck mit Seitenlänge seite.
    """
    forward(seite)
    left(120)
    forward(seite)
    left(120)
    forward(seite)
    left(120)

reset()
pensize(5)
pencolor("red")

kurz = 60
lang = 180

right(120)
seite = lang
dreieck()
left(180)
dreieck()

left(90)

seite = kurz
dreieck()
left(180)
dreieck()

hideturtle()
