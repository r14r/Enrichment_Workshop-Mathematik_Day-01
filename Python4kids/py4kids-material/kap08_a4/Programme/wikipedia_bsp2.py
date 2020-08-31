# Python für Kids -- 4. Auflage, Kapitel 8

# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# wikipedia_bsp2.py : Eine Superrosette mit 36 Blättern und
#                     veränderlichem Farbverlauf

from turtle import *
from mytools import jump

def n_eck(eckenzahl, seitenlaenge):
    drehwinkel = 360.0 / eckenzahl
    blau = 1.0
    aenderung = -2.0 / eckenzahl
    for i in range(eckenzahl):
        rot = 1.0 - blau
        pencolor(rot, 0, blau)
        forward(seitenlaenge)
        left(drehwinkel)
        if i == eckenzahl // 2:
            aenderung = -aenderung
        blau = blau + aenderung

def rosette(eckenzahl, blattzahl, seite):
    drehwinkel = 360 / blattzahl
    for i in range(blattzahl):
        tracer(False)
        n_eck(eckenzahl, seite)
        tracer(True)
        left(drehwinkel)

def super_rosette(eckenzahl, seite):
    rosette(eckenzahl, eckenzahl, seite)

if __name__ == "__main__":
    title("Turtlegrafik - Wikipedia Beispiel Nr. 2")
    setup(500, 500)
    reset()
    bgcolor("black")
    pencolor("red")
    pensize(3)
    super_rosette(36, 20)
    hideturtle()
    
