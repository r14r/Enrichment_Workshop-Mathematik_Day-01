# Python für Kids (4. Auflage) - Kapitel 14
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum: 20. 8. 2009
# dynaspiralen_arbeit.py

from turtle import Turtle, Screen

screen = Screen()

alex = Turtle()
bert = Turtle()
bert.left(90)
bert.color("red")
carl = Turtle()
carl.color("green")
carl.left(180)
dinu=Turtle()
dinu.left(270)
dinu.color("blue")
kroeten = (alex, bert, carl, dinu)

for krot in kroeten:
    krot.hideturtle()
    krot.speed(0)
    krot.penup()      # funktioniert wie jump(50)
    krot.forward(50)  # schön wäre statt dessen:
    krot.pendown()    # krot.jump(50)
    krot.pensize(3)
    krot.right(30)
    
for laenge in range(100, 0, -5):
    screen.tracer(False)
    for krot in kroeten:
        krot.forward(laenge)
        krot.left(120)
    screen.tracer(True)
