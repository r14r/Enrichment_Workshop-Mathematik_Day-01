# Python für Kids -- 4. Auflage, Kapitel 13
# Autor: Gregor Lingl
# Datum 18. 8. 2009
# uhr_arbeit.py

# mit Minutenzeiger
# ... mach weiter!

from turtle import *
from mytools import jump
from datetime import datetime

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

def tick():
    jetzt = datetime.now()
    sekunden=jetzt.second + jetzt.microsecond * 0.000001
#    print("{0:8.2f}".format(sekunden))
    sekundenzeiger.setheading(6*sekunden)     # 360/60
    minuten = jetzt.minute + sekunden/60
    minutenzeiger.setheading(6*minuten)
    screen.ontimer(tick, 200)
    
def uhr():
    global sekundenzeiger, minutenzeiger
    screen.setup(400, 400)
    screen.title("Die Krötenuhr")
    shape("turtle")
    mache_zeiger_shape("sekundenzeiger", 120, 25)
    mache_zeiger_shape("minutenzeiger", 130, 25)
    ziffernblatt(160)
    sekundenzeiger = Turtle(shape="sekundenzeiger")
    sekundenzeiger.shapesize(1, 1, 3)
    sekundenzeiger.color("red", "blue")
    sekundenzeiger.speed(0)
    minutenzeiger = Turtle(shape="minutenzeiger")
    tick()
    
if __name__ == "__main__":
    screen = Screen()    
    uhr()
