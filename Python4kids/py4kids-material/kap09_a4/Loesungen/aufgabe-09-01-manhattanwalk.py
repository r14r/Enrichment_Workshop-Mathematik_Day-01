# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# manhattanwalk.py   -  Lösung von Kapitel 9, Aufgabe 1

from turtle import *
import random

def zufallsschritt(laenge):
    winkel = random.randint(-1,2) * 90
    left(winkel)
    forward(laenge)

def zufallsweg(schritt_anzahl, schrittlaenge, torkelwinkel):
    pu(); home(); pd()
    startwinkel = random.randint(0,359)
    right(startwinkel)
    for i in range(schritt_anzahl):
        zufallsschritt(schrittlaenge)

def randomwalk(entfernung, schrittlaenge, maxwinkel=180):
    pu(); home(); pd()
    startwinkel = random.randint(0,3) * 90.0
    right(startwinkel)
    start = position()
    while distance(start) < entfernung:
        zufallsschritt(schrittlaenge)

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
    randomwalk_test(10)
    
