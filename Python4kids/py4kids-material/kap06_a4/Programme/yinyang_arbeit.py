# Python für Kids -- 4. Auflage, Kapitel 6
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# yinyang03.py : interaktive Entwicklung, bottom-up
#                Vier unterschiedliche Yinyang-Symbole

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
    dot(radius / 3, gegenfarbe)
    jump(radius / 2, 90)

def yinyang(radius, farbe="white",
            gegenfarbe="black", strichdicke=3):
    """kombiniert zwei halbe zu einem ganzen Yinyang-Symbol.
       Farben und Strichdicke über Parameter einstellbar!
    """
    pensize(strichdicke)
    yin(radius, farbe, gegenfarbe)
    left(180)
    yin(radius, gegenfarbe, farbe)
    left(180)
    

reset()
hideturtle()
speed(0)

jump(80,45)
yinyang(45, "gray80", "maroon")
jump(126,180)
right(90)
yinyang(65, strichdicke=2)
jump(-134)
yinyang(45, "red", "green")
left(90)
jump(126)
yinyang(65, strichdicke=5)

