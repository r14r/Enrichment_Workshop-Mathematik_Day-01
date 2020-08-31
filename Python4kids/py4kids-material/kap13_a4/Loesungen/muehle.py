# Python für Kids -- 4. Auflage, Kapitel 13
# Autor: Gregor Lingl
# Datum: 12. 10. 2009
# Lösungen r Aufgaben

from turtle import *

def main():
    reset()
    setup(640, 480)
    title("Turtle-Grafik: Mühle")
    speed(1)
    rt(15)

    # dreiflügelige Turtleform erzeugen
    begin_poly()
    for i in range(3):
        fd(120)
        if i == 0:
            x=xcor() # turtle misst die Länge
                     # der halben Basis des Dreiecks
        lt(105)
        fd(2*x)
        lt(105)
        fd(120)
        rt(90)
    end_poly()
    register_shape('muehle', get_poly())

    # Die Mühle
    reset()
    speed(1)
    pu()
    bk(120)
    pd()
    pensize(15)
    pencolor("blue")
    fd(180)
    
    # das Rad ...
    shape('muehle')
    shapesize(outline=7)
    pu()
    color("green","red")
    # .. dreht sich
    winkelgeschwindigkeit=3.6
    speed(5)
    for i in range(360):
        lt(winkelgeschwindigkeit)
        winkelgeschwindigkeit -= 0.0095

if __name__ == '__main__':
    main()
##    mainloop()
