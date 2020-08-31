# Python für Kids -- 4. Auflage, Kapitel 13
# Autor: Gregor Lingl
# Datum 18. 8. 2009
# uhr_arbeit.py  

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

def wochentag(t):
    wochentag = ["Montag", "Dienstag", "Mittwoch",
        "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "März.", "April", "Mai", "Juni",
             "Juli", "Aug.", "Sep.", "Okt.", "Nov.", "Dez."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "{0} {1} {2}".format(m, t, j)

def tick():
    jetzt = datetime.now()
    sekunden=jetzt.second + jetzt.microsecond * 0.000001
    minuten = jetzt.minute + sekunden/60
    stunden = jetzt.hour + minuten/60
    screen.tracer(False)
    writer.clear()
    writer.home()
    writer.forward(65)
    writer.write(wochentag(jetzt),
                 align="center", font=("Courier", 14, "bold"))
    writer.back(155)
    writer.write(datum(jetzt),
                 align="center", font=("Courier", 14, "bold"))      
    sekundenzeiger.setheading(6*sekunden)     # 360/60
    minutenzeiger.setheading(6*minuten)
    stundenzeiger.setheading(30*stunden)
    screen.tracer(True)
    screen.ontimer(tick, 200)
    
def uhr():
    global sekundenzeiger, minutenzeiger, stundenzeiger, writer
    screen.setup(400, 400)
    screen.clear()
    screen.title("Python Turtle-Grafik: Die Uhr")
    screen.tracer(False)
    shape("turtle")
    mache_zeiger_shape("sekundenzeiger", 120, 25)
    mache_zeiger_shape("minutenzeiger", 130, 25)
    mache_zeiger_shape("stundenzeiger", 90, 25)
    ziffernblatt(160)
    sekundenzeiger = Turtle(shape="sekundenzeiger") # Schlüsselwortargument!
    sekundenzeiger.color("gray20", "gray80")
    minutenzeiger = Turtle(shape="minutenzeiger")
    minutenzeiger.color("blue1", "red1")
    stundenzeiger = Turtle(shape="stundenzeiger")
    stundenzeiger.color("blue3", "red3")
    for zeiger in sekundenzeiger, minutenzeiger, stundenzeiger:
        zeiger.shapesize(1, 1, 3)
        zeiger.speed(0)
    writer = Turtle(visible=False)
    writer.penup()
    screen.tracer(True)
    tick()
    
if __name__ == "__main__":
    screen = Screen()    
    uhr()
