# Python für Kids (4. Auflage) - Kapitel 8
# Autor: Gregor Lingl
# Datum: 9. 8. 2008
# peace02 : Zeichnen des peace Logos auf Regenbogenfahne.

from turtle import *
from mytools import jump

friedensfarben = ["red3", "orange", "yellow", "seagreen4",
                  "orchid4", "royalblue1", "dodgerblue4"]

streifenbreite = 44

def streifen(laenge, breite, farbe):
    pensize(breite),
    pencolor(farbe),
    forward(laenge)
    jump(-laenge)

def fahne():
    jump(-3 * streifenbreite)
    right(90)
    jump(-200)

    for farbe in friedensfarben:
        streifen(400, streifenbreite, farbe)
        jump(streifenbreite, -90)
    penup()
    home()
    pendown()

def kreis(radius):
    jump(radius, 90)
    circle(radius)
    jump(radius, -90)

def logo(radius):
    pencolor("white")
    pensize(radius/6.0)
    kreis(radius)
    for winkel in (135, 180, 225, 0):
        setheading(winkel)
        streifen(radius, radius/6.0, "white")

def peace():    
    fahne()
    logo(120)
    hideturtle()

reset()
tracer(False)
peace()
tracer(True)
