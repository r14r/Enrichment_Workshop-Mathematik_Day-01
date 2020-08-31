# -*- coding: cp1252 -*-

# Python für Kids -- 3. Auflage, Kapitel 5

# Autor: Gregor Lingl
# Datum: 20. 3. 2008
# dreieck_arbeit_.py
# Zum Einstieg in 'Funktionen mit Parametern'

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
pensize(10)
right(90)

pencolor("red")
seite = 65
dreieck()
left(120)
      
pencolor("green")
seite = 100
dreieck()
left(120)

pencolor("blue")
seite = 135
dreieck()
left(120)

hideturtle()
