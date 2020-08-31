# Python für Kids -- 4. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 5. 8. 2009
# quadrat06.py: 6 gefüllte Quadrate in verschiedenen Farben
#               und verschiedenen Größen zeichnen

from turtle import *

startseite = 110
aenderung = -5

reset()
pensize(5)

right(45)                  # Das isses!

seite = startseite
pencolor("red")
fillcolor("cyan")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)
seite = seite + aenderung

pencolor("green")
fillcolor("magenta")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)
seite = seite + aenderung

pencolor("blue")
fillcolor("yellow")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("cyan")
fillcolor("red")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("green")
fillcolor("cyan")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("yellow")
fillcolor("blue")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)
