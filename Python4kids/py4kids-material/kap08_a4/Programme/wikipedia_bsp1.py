# Python für Kids -- 4. Auflage, Kapitel 8

# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# wikipedia_bsp1.py : Eine Superrosette mit 36 Blättern
# siehe dazu: http://de.wikipedia.org/wiki/Logo_(Programmiersprache)

from turtle import *
from mytools import jump

def n_eck(eckenzahl, seitenlaenge):
    drehwinkel = 360.0 / eckenzahl
    for i in range(eckenzahl):
        forward(seitenlaenge)
        left(drehwinkel)

def rosette(eckenzahl, blattzahl, seite):
    drehwinkel = 360.0 / blattzahl
    for i in range(blattzahl):
        tracer(False)
        n_eck(eckenzahl, seite)
        tracer(True)
        left(drehwinkel)

def super_rosette(eckenzahl, seite):
    rosette(eckenzahl, eckenzahl, seite)

if __name__ == "__main__":
    title("Turtlegrafik - Wikipedia Beispiel Nr. 1")
    setup(500, 500)
    reset()
    bgcolor("black")
    pencolor("red")    
    super_rosette(36, 20)
    hideturtle()
    
