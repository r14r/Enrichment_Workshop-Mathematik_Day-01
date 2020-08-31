# Python für Kids -- 4. Auflage, Kapitel 8

# Autor: Gregor Lingl
# Datum: 9. 8. 2009
# polygon.py :   Regelmäßige n-Ecke (Polygone)
#                    und Kombinationen daraus

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
        n_eck(eckenzahl, seite)
        left(drehwinkel)

def super_rosette(eckenzahl, seite):
    rosette(eckenzahl, eckenzahl, seite)

def super_rosette_demo():
    reset()
    pensize(3)
    super_rosette(3, 55)
    jump(120, -90)
    super_rosette(8, 20)
    jump(240, 90)
    super_rosette(11, 18)


#print "Name:", __name__

if __name__ == "__main__":
    super_rosette_demo()        
        
