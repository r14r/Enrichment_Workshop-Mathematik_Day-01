# Python für Kids -- 4. Auflage, Kapitel 2
# Autor: Gregor Lingl
# Datum: 5. 8. 2009
# quadrat03.py: 6 gefüllte Quadrate in verschiedenen Farben
#               zeichnen

from turtle import *

reset()
pensize(5)

right(45)             # Das isses!

pencolor("red")
fillcolor("cyan")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

right(60)

pencolor("green")
fillcolor("magenta")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

right(60)

pencolor("blue")
fillcolor("yellow")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

right(60)

pencolor("cyan")
fillcolor("red")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

right(60)

pencolor("magenta")
fillcolor("green")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

right(60)

pencolor("yellow")
fillcolor("blue")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()

right(60)
