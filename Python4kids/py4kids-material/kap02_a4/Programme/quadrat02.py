# Python für Kids -- 4. Auflage, Kapitel 2
# Autor: Gregor Lingl
# Datum: 5. 8. 2009
# quadrat02.py: Ein rotes Quadrat, das auf der Spitze
#               steht, zeichnen.

from turtle import *

reset()
pensize(5)

right(45)         # Das isses!

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
