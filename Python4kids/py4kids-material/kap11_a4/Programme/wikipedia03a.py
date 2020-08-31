# Python für Kids (4. Auflage) - Kapitel 11
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum 12. 8. 2009
# wikipedia03.py     -   2. Fassung

from turtle import Screen, Turtle
from mytools import frange

def myturtle(winkel):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(2)
    turtle.setheading(winkel)
    return turtle

def parallel_super_rosette(ecken, seite):
    winkel = 360.0 / ecken
    turtles = [myturtle(i*winkel) for i in range(ecken)]
    blauwerte = [abs(k) for k in frange(-1, 1, 2/ecken)]
    for blau in blauwerte:
        rot = 1.0 - blau
        for turtle in turtles:
            turtle.pencolor(rot, 0, blau)
            turtle.forward(seite)
            turtle.left(winkel)
        screen.update()
    

def main():
    global screen
    screen = Screen()
    screen.title("Turtle-Grafik - Wikipedia Bsp. 3a")
    screen.resetscreen()
    screen.setup(500, 500)
    screen.tracer(False)
    screen.bgcolor("black")
    parallel_super_rosette(9, 80)

if __name__ == "__main__":
    main()
    
