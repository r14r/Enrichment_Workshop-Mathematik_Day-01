# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# randomwalk03.py

from turtle import *
import random

def zufallsschritt(laenge, maxwinkel):
    winkel = random.randint(-maxwinkel,maxwinkel)
    left(winkel)
    forward(laenge)

def randomwalk(entfernung, schrittlaenge, maxwinkel=180):
    pu(); home(); pd()
    startwinkel = random.randint(0, 359)
    right(startwinkel)
    start = position()
    while distance(start) < entfernung:
        zufallsschritt(schrittlaenge, maxwinkel)

def randomwalk_test(anzahl_walks):
    reset()
    setup(400,400)
    speed(0)
    pensize(1)
    for i in range(anzahl_walks):
        pencolor("black")
        randomwalk(150, 15)
        pencolor("red")
        stamp()

if __name__ == "__main__":
    randomwalk_test(6)
