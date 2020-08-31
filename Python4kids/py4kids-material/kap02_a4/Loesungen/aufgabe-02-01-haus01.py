# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum 5. 8. 2009
# haus.py: Kapitel 2: Aufgabe 1

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
pencolor("red")
forward(150)
left(120)
forward(150)
left(120)
forward(150)
left(120)

hideturtle()
