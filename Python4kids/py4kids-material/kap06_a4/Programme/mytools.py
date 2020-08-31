# Python für Kids -- 4. Auflage, Kapitel 5

# Autor: Gregor Lingl
# Datum: 6. 8. 2008

# mytools.py : Meine Bibliothek von selbst erstellten 
# brauchbaren Funktionen für die Arbeit mit Python für Kids.

from turtle import *

def jump(distanz, winkel=0):
    """springt um eine Strecke der Länge distanz
    in die Richtung von winkel"""
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()
