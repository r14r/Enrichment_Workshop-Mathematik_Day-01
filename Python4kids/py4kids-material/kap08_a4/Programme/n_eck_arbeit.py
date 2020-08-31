# Python für Kids (4. Auflage) - Kapitel 8
# Autor: Gregor Lingl
# Datum: 9. 8. 2009
# n_eck.py  : n-Ecke

from turtle import *
from mytools import jump

def n_eck(eckenzahl, seitenlaenge):
    drehwinkel = 360 / eckenzahl
    for i in range(eckenzahl):
        forward(seitenlaenge)
        left(drehwinkel)

def rosette(ecken, blaetter, seite):
    for i in range(blaetter):
        tracer(False)
        n_eck(ecken, seite)
        tracer(True)
        left(360/blaetter)
        
def super_rosette(ecken, seite):
    rosette(ecken, ecken, seite)

if __name__ == '__main__':
    title("turtle . Wikipedia Beispiel Nr. 1")
    reset()
    bgcolor("black")
    setup(500,500)
    pencolor("red")
    super_rosette(36, 20)
