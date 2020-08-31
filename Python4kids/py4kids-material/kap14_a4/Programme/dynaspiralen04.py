# Python für Kids (4. Auflage) - Kapitel 14
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum: 20. 8. 2009
# dynaspiralen_arbeit.py

from turtle import Turtle, Screen

class MyTurtle(Turtle):
    
    def jump(self, laenge):
        self.penup()
        self.forward(laenge)
        self.pendown()

    def polyschritt(self, laenge, winkel):
        self.forward(laenge)
        self.left(winkel)

screen = Screen()

alex = MyTurtle()
bert = MyTurtle()
bert.left(90)
bert.color("red")
carl = MyTurtle()
carl.color("green")
carl.left(180)
dinu = MyTurtle()
dinu.left(270)
dinu.color("blue")
kroeten = (alex, bert, carl, dinu)

for krot in kroeten:
    krot.hideturtle()
    krot.speed(0)
    krot.jump(50)
    krot.pensize(3)
    krot.right(30)
    
for laenge in range(100, 0, -5):
    screen.tracer(False)
    for krot in kroeten:
        krot.polyschritt(laenge, 120)
    screen.tracer(True)
