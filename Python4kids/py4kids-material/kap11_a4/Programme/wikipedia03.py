# Python für Kids (4. Auflage) - Kapitel 11
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum 12. 8. 2009
# wikipedia_arbeit.py  

from turtle import Screen, Turtle
from mytools import krange

def myturtle(winkel):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(2)
    turtle.setheading(winkel)
    return turtle

def parallel_super_rosette(ecken, seite):
    winkel = 360 / ecken
    turtles = [myturtle(i*winkel) for i in range(ecken)]
    blauwerte = [abs(k) for k in krange(-1, 1, 2/ecken)]
    for blau in blauwerte:
        rot = 1.0 - blau
        screen.tracer(False)
        for turtle in turtles:
            turtle.pencolor(rot, 0, blau)
            turtle.forward(seite)
            turtle.left(winkel)
        screen.tracer(True)
    

def main():
    global screen
    screen = Screen()
    screen.title("Turtle-Grafik - Wikipedia Bsp. 3")
    screen.clearscreen()   
    screen.setup(500, 500)
    screen.bgcolor("black")
    screen.tracer(False)
    parallel_super_rosette(36, 20)

if __name__ == "__main__":
    main()
    
