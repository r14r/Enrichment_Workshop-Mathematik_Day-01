# Python für Kids -- 4. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 5. 8. 2008
# dreieck04.py:  3 gleichseitige farbige, gefüllte Dreiecke

from turtle import *

reset()
pensize(10)
right(90)

pencolor("red")
fillcolor("cyan")

begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
end_fill()

left(120)

pencolor("green")
fillcolor("magenta")


begin_fill()
forward(135)
left(120)
forward(135)
left(120)
forward(135)
left(120)
end_fill()

left(120)

pencolor("blue")
fillcolor("yellow")

begin_fill()
forward(65)
left(120)
forward(65)
left(120)
forward(65)
left(120)
end_fill()

left(120)

hideturtle()
