# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# quadrat09.py: Kapitel 4, Aufgabe 3
# Entwickelt aus quadrat06.py

from turtle import *

def quadrat():
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)

def fuelle_quadrat():
    begin_fill()
    quadrat()
    end_fill()

startseite = 110
aenderung = -5

reset()
pensize(5)

left(45)             # Das isses!

seite = startseite
pencolor("red")
fillcolor("cyan")
fuelle_quadrat()

right(60)

seite = seite + aenderung
pencolor("green")
fillcolor("magenta")
fuelle_quadrat()

right(60)

seite = seite + aenderung
pencolor("blue")
fillcolor("yellow")
fuelle_quadrat()

right(60)

seite = seite + aenderung
pencolor("cyan")
fillcolor("red")
fuelle_quadrat()

right(60)

seite = seite + aenderung
pencolor("magenta")
fillcolor("green")
fuelle_quadrat()

right(60)

seite = seite + aenderung
pencolor("yellow")
fillcolor("blue")
fuelle_quadrat()

right(60)
