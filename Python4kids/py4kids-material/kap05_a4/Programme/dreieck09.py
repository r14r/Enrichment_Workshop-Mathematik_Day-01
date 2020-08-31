# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# dreieck09.py
# Zum Einstieg in 'Funktionen mit Parametern'.

from turtle import *

def dreieck(laenge):
    """zeichne Dreieck mit Seitenlänge seite.
    """
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)

reset()
pensize(10)
right(90)

pencolor("red")
dreieck(65)
left(120)
      
pencolor("green")
dreieck(100)
left(120)

pencolor("blue")
dreieck(135)
left(120)

hideturtle()
