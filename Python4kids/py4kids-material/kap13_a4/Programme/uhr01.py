# Python für Kids -- 4. Auflage, Kapitel 13
# Autor: Gregor Lingl
# Datum 18. 8. 2009
# uhr_01.py  

from turtle import *
from mytools import jump

def zeiger(laenge, spitze):
    fd(laenge)
    rt(90)
    fd(spitze/2)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2)

def mache_zeiger_shape(name, laenge, spitze):
    reset()
    begin_poly()
    zeiger(laenge, spitze)
    end_poly()
    zeiger_form = get_poly()
    screen.register_shape(name, zeiger_form)

def ziffernblatt(radius):
    reset()
    pensize(7)
    for i in range(12):
        jump(radius)
        fd(25)
        jump(-radius-25)
        rt(30)
    hideturtle()

def uhr():
    global sekundenzeiger
    screen.setup(400, 400)
    screen.title("Die Krötenuhr")
    shape("turtle")
    mache_zeiger_shape("sekundenzeiger", 130, 25)
    ziffernblatt(160)
    sekundenzeiger = Turtle()
    sekundenzeiger.shape("sekundenzeiger")
    sekundenzeiger.shapesize(1, 1, 3)
    sekundenzeiger.color("red", "blue")
    sekundenzeiger.speed(1)
    
if __name__ == "__main__":
    screen = Screen()    
    uhr()
