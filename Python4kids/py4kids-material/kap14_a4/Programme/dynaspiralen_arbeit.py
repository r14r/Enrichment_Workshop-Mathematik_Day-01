# Python für Kids (4. Auflage) - Kapitel 14
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum: 20. 8. 2009
# dynaspiralen_arbeit.py  -  mit Konstruktor

from turtle import Turtle, Screen

class MyTurtle(Turtle):

    def __init__(self, farbe="black", winkel=0, strich=1):
        Turtle.__init__(self)
        self.color(farbe)
        self.left(winkel)
        self.pensize(strich)
    
    def jump(self, laenge):
        self.penup()
        self.forward(laenge)
        self.pendown()

    def polyschritt(self, laenge, winkel):
        self.forward(laenge)
        self.left(winkel)

screen = Screen()

alex = MyTurtle("pink", 0, 3)
bert = MyTurtle("red", 90, 3)
carl = MyTurtle("green", 180, 3)
dinu = MyTurtle("blue", 270, 3)
kroeten = (alex, bert, carl, dinu)

for krot in kroeten:
    krot.hideturtle()
    krot.speed(0)
    krot.jump(50)
    krot.right(30)
    
for laenge in range(100, 0, -5):
    screen.tracer(False)
    for krot in kroeten:
        krot.polyschritt(laenge, 120)
    screen.tracer(True)
