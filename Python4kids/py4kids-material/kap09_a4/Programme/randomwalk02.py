# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# randomwalk01.py

from turtle import *
import random

def zufallsschritt(laenge, maxwinkel):
    winkel = random.randint(-maxwinkel,maxwinkel)
    left(winkel)
    forward(laenge)

def zufallsweg(schritt_anzahl, schrittlaenge, torkelwinkel):
    pu(); home(); pd()
    startwinkel = random.randint(0,359)
    right(startwinkel)
    for i in range(schritt_anzahl):
        zufallsschritt(schrittlaenge, torkelwinkel)

def randomwalk_test(anzahl_walks):
    reset()
    setup(400,400)
    speed(0)
    pensize(3)
    for i in range(anzahl_walks):
        zufallsweg(10, 15, 90)

if __name__ == "__main__":
    randomwalk_test(10)
