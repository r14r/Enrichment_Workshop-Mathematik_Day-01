# Python für Kids (4. Auflage) - Kapitel 11
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum: 11. 8. 2009
# vierturtles.py

from turtle import Turtle

alex = Turtle()
bert = Turtle()
alex.forward(50)
bert.left(90)
bert.color("red")
bert.forward(50)
carl = Turtle()
carl.color("green")
carl.left(180)
carl.forward(50)
dinu=Turtle()
dinu.left(270)
dinu.color("blue")
dinu.forward(50)
kroeten = (alex, bert, carl, dinu)

for krot in kroeten:
    krot.pensize(3)
    krot.right(30)
    
for i in range(3):
    for krot in kroeten:
        krot.forward(100)
        krot.left(120)
