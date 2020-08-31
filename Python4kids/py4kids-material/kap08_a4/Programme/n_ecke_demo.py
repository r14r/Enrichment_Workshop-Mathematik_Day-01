# Python für Kids -- 4. Auflage, Kapitel 8

# Autor: Gregor Lingl
# Datum: 9. 8. 2009
# n_ecke_demo.py :   Regelmäßige n-Ecke (Polygone)

from turtle import *
from mytools import jump

def n_eck(seitenlaenge, anzahl_ecken):
    drehwinkel = 360/anzahl_ecken
    for i in range(anzahl_ecken):
        forward(seitenlaenge)
        left(drehwinkel)
       
def n_eck_demo():
    reset()
    speed(1)
    title("Python - Turtle : n-Ecke")
    pensize(3)
    right(90)
    jump(-185)
    for ecken in range(3, 7):
        n_eck(40, ecken)
        jump(ecken*24)

#if __name__ == '__main__':
n_eck_demo()
