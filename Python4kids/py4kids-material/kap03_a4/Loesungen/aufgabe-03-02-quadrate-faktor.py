# Python für Kids -- . Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# aufgabe-03-02.py - Kapitel 3, Aufgabe 2

# Turtle-Grafik, 6 Quadrate, verschieden groß!
# Variable: seite, startseite, faktor
# Für jedes Quadrat wird seite aus der Seite des vorigen
# Quadrats berechnet: NEU: seite = seite * faktor
# Benutzereingabe für startseite und aenderung

from turtle import *

title("Turtle-Grafik: Sechs verschieden große Quadrate.")

prompt = """Dieses Programm zeichnet sechs
gegeneinander verdrehte Quadrate mit wachsender
oder abnehmender Größe.

Wie lang ist die Seitenlänge des ersten Quadrats?"""
startseite = numinput("6 gedrehte Quadrate", prompt)

prompt = """Dieses Programm zeichnet sechs
gegeneinander verdrehte Quadrate mit wachsender
oder abnehmender Größe.

Der Längenunterschied aufeinanderfolgender Seiten
wird durch einen Faktor festgelegt.
Wie groß soll dieser Faktor sein?"""
faktor = numinput("6 gedrehte Quadrate", prompt)

seite = startseite

reset()
width(5)
left(45)

color("red")

forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)

seite = seite * faktor
right(60)
color("yellow")

forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)

seite = seite * faktor
right(60)
color("green")

forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)

seite = seite * faktor
right(60)
color("cyan")

forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)


seite = seite * faktor
right(60)
color("blue")

forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)

seite = seite * faktor
right(60)
color("magenta")

forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)

right(60)

hideturtle()
