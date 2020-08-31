# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# randomwalk01.py

from turtle import *
import random

def zufallsschritt():
    winkel = random.randint(-30, 30)
    left(winkel)
    forward(15)

setup(400, 400)
penup()
home()
pendown()
pensize(3)

startwinkel = random.randint(0,359)
right(startwinkel)

for n in range(10):
    zufallsschritt()
