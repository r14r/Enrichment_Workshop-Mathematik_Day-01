# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum 5. 8. 2009
# haus02.py: Kapitel 2 : Aufgabe 5

from turtle import *

reset()

penup()
back(25)
right(90)
back(60)
pendown()

# Wand
pensize(3)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
right(90)
forward(70)
right(90)

penup()
back(15)
pendown()

# Dach
pensize(5)
pencolor("darkred")
fillcolor("red")
begin_fill()
forward(150)
left(120)
forward(150)
left(120)
forward(150)
left(120)
end_fill()

# Fenster
penup()
forward(25)
right(90)
forward(10)
pensize(1)
pencolor("black")
fillcolor("yellow")
pendown()
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()

# Türe
penup()
left(90)
forward(60)
right(90)
pendown()
fillcolor("brown")
begin_fill()
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
end_fill()

hideturtle()
