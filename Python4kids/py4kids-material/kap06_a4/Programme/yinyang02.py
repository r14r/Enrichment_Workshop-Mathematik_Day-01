# Python für Kids -- 4. Auflage, Kapitel 6
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# yinyang02.py : interaktive Entwicklung, bottom-up

from turtle import *
from mytools import jump

def yin(radius, farbe, gegenfarbe):
    """Zeichne halbes Yinyang-Symbol
    """
    fillcolor(farbe)
    begin_fill()
    circle(radius / 2, 180)
    circle(radius, 180)
    left(180)
    circle(-radius / 2,180)
    end_fill()
    jump(radius / 2, -90)
    dot(radius / 4, gegenfarbe)
    jump(radius / 2, 90)

def yinyang(radius):
    """kobiniert zwei halbe zu einem ganzen Yinyang-Symbol.
    """
    pensize(3)
    yin(radius, "white", "black")
    left(180)
    yin(radius, "black", "white")
    left(180)
    

reset()
yinyang(125)
hideturtle()
