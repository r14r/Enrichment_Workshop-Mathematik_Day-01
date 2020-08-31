# Python für Kids (4. Auflage) - Kapitel 13
# Ereignisgesteuerte Programme

# Autor: Gregor Lingl
# Datum 16. 8. 2009

# scribble - ein einfaches Zeichenprogramm

# (1) Stift zeichnet eine Linie zur (links) angeklickten Stelle
# (2) Stift springt (ohne Zeichnen) zur mit mittlerer Taste
#     angeklickten Stelle
# (3) Stift kritzelt, wenn er gezogen wird
# (4) rechte Maustaste schaltet füllen ein und aus
# (5) undo() - Funktion des Stiftes an BackSpace-Taste binden
#     clear() - Funktion des Stiftes an die Leertaste binden

from turtle import Screen, Turtle
import sys
sys.setrecursionlimit(20000)

def jump(x, y):
    stift.penup()
    stift.goto(x, y)
    stift.pendown()

def fuellenumschalten(xdummy, ydummy):
    if stift.filling():
        stift.end_fill()
        stift.fillcolor("")
    else:
        stift.begin_fill()
        stift.fillcolor("black") 

screen = Screen()
screen.clear()
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)

screen.onclick(stift.goto)
screen.onclick(jump, 2)
screen.onclick(fuellenumschalten, 3)
stift.ondrag(stift.goto)

screen.onkeypress(stift.undo, "BackSpace")
screen.onkeypress(stift.clear, "space")
screen.listen()
