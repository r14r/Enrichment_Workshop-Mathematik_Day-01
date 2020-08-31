# Python für Kids (4. Auflage) - Kapitel 13
# Ereignisgesteuerte Programme

# Autor: Gregor Lingl
# Datum 16. 8. 2009

# scribble - ein einfaches Zeichenprogramm

# (1) Stift zeichnet eine Linie zur (links) angeklickten Stelle
# (2) Stift springt (ohne Zeichnen) zur mit mittlerer Taste
#     angeklickten Stelle

from turtle import Screen, Turtle

def jump(x, y):
    stift.penup()
    stift.goto(x, y)
    stift.pendown()

screen = Screen()
screen.clear()
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)

screen.onclick(stift.goto)
screen.onclick(jump, 2)
