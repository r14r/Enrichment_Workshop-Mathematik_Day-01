## Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# aufgabe-04-05-yinyang.py: Kapitel 4, Aufgabe 5

from turtle import *

reset()
pensize(3)
circle(60, 180)
circle(120, 180)

fillcolor("black")
begin_fill()
circle(120, 180)
left(180)
circle(-60, 180)
circle(60, 180)
end_fill()

left(90)
penup()
forward(160)
right(90)
begin_fill()
circle(20)
end_fill()

right(90)
forward(80)
right(90)
fillcolor("white")
begin_fill()
circle(20)
end_fill()

home()
hideturtle()
