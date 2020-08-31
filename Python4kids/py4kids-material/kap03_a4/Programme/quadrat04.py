# Python für Kids -- 4. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 5. 8. 2009
# quadrat04.py: 6 gefüllte Quadrate in verschiedenen Farben
#               und verschiedenen Größen zeichnen

from turtle import *

reset()
pensize(5)

right(45)             # Das isses!

seite = 100
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

seite = 85
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

seite = 70
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

seite = 55
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

seite = 40
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

seite = 25
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
