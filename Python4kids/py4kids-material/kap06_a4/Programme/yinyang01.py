# Python für Kids -- 4. Auflage, Kapitel 6
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# yinyang01.py # Übersetzung des Pseudocodes aus Kapitel 6

from turtle import *
from mytools import jump

def punkt(radius, farbe):
    "Zeichen Kreis mit Turtleposition als Mittelpunkt."
    jump(radius, 90)
    color(farbe)
    begin_fill()
    circle(radius)
    end_fill()
    jump(radius, -90)
    
def yinfigur(radius, farbe):
    "Zeichne gefülltes Feld für halbes Yinyang-Symbol"
    r2 = radius/2.0
    fillcolor(farbe)
    begin_fill()
    circle(r2, 180)
    circle(radius, 180)
    left(180)
    circle(-r2, 180) 
    end_fill()

def yin(durchmesser, feldfarbe, punktfarbe):
    "Zeichne halbes Yinyang-Symbol."
    radius = durchmesser / 2
    r2 = radius / 2
    rp = r2 / 4
    pencolor("black")
    yinfigur(radius, feldfarbe)
    jump(r2, -90)
    punkt(rp, punktfarbe)
    jump(r2, 90)

def yinyang(durchmesser):
    "Zeichne Yinyang-Symbol"
    pensize(3)
    yin(durchmesser, "white", "black")
    left(180)
    yin(durchmesser, "black", "white")

reset()
yinyang(200)
hideturtle()
