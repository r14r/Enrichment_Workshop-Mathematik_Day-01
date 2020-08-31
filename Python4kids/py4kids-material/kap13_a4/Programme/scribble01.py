# Python für Kids (4. Auflage) - Kapitel 13
# Ereignisgesteuerte Programme

# Autor: Gregor Lingl
# Datum 16. 8. 2009
# scribble - ein einfaches Zeichenprogramm

# (1) Stift zeichnet eine Linie zur (links) angeklickten Stelle

from turtle import Screen, Turtle

screen = Screen()
screen.clear()
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)

screen.onclick(stift.goto)
