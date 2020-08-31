# Python für Kids -- 43. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# quadrat10.py: gefüllte Quadrate in verschiedenen Farben
#               zeichnen
# Mit Eingabe-Dialogen
# auch für die Anzahl der Quadrate.


from turtle import *

def quadrat():
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)

def fuelle_quadrat():
    begin_fill()
    quadrat()
    end_fill()


title("Turtle-Grafik: Gegeneinander gedrehte Quadrate.")

prompt = """Dieses Programm zeichnet bis zu sechs
gegeneinander verdrehte Quadrate.

Wie lang ist die Seitenlänge des ersten Quadrats?"""
startseite = numinput("Gedrehte Quadrate", prompt)

prompt = """Dieses Programm zeichnet bis zu sechs
gegeneinander verdrehte Quadrate.

Wie groß ist der Längenunterschied zwischen den
Seiten aufeinanderfolgender Quadrate?"""
aenderung = numinput("Gedrehte Quadrate", prompt)

prompt = """Dieses Programm zeichnet bis zu sechs
gegeneinander verdrehte Quadrate.

Wie viele Quadrate sollen gezeichnet werden(2-6)?"""
anzahl = numinput("Gedrehte Quadrate", prompt, 4, 2, 6)


reset()
speed(10)
pensize(5)

left(45)      # Mit left sieht's besser aus
              # (finde ich)
seite = startseite
drehwinkel = 360 / anzahl
pencolor("red")
fillcolor("cyan")
fuelle_quadrat()

right(drehwinkel)

seite = seite + aenderung
pencolor("green")
fillcolor("magenta")
fuelle_quadrat()

right(drehwinkel)

if anzahl > 2:
    seite = seite + aenderung
    pencolor("blue")
    fillcolor("yellow")
    fuelle_quadrat()
    right(drehwinkel)

if anzahl > 3:
    seite = seite + aenderung
    pencolor("cyan")
    fillcolor("red")
    fuelle_quadrat()
    right(drehwinkel)

if anzahl > 4:
    seite = seite + aenderung
    pencolor("green")
    fillcolor("cyan")
    fuelle_quadrat()
    right(drehwinkel)

if anzahl > 5:
    seite = seite + aenderung
    pencolor("yellow")
    fillcolor("blue")
    fuelle_quadrat()
    right(drehwinkel)

# wir übermalen die Hälfte des 1. Quadrats
# noch einmal

if anzahl > 4:
    seite = startseite
    pencolor("red")
    fillcolor("cyan")

    left(90)
    begin_fill()
    forward(seite)
    right(90)
    forward(seite)
    end_fill()       # dirty hack!

hideturtle()
