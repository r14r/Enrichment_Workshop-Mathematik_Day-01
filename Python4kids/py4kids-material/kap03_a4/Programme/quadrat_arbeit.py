# Python für Kids -- 43. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# quadrat07.py: 6 gefüllte Quadrate in verschiedenen Farben
#               zeichnen
# Mit Eingabe-Dialogen

from turtle import *

title("Turtle-Grafik: Sechs gegeneinander gedrehte Quadrate.")

prompt = """Dieses Programm zeichnet sechs
gegeneinander verdrehte Quadrate.

Wie lang ist die Seitenlänge des ersten Quadrats?"""
startseite = numinput("6 gedrehte Quadrate", prompt)
prompt = """Dieses Programm zeichnet sechs
gegeneinander verdrehte Quadrate.

Wie groß ist der Längenunterschied zwischen den
Seiten aufeinanderfolgender Quadrate?"""
aenderung = numinput("6 gedrehte Quadrate", prompt)

reset()
speed(10)
pensize(5)

left(45)      # Mit left sieht's besser aus
              # (finde ich)
seite = startseite
pencolor("red")
fillcolor("cyan")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("green")
fillcolor("magenta")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("blue")
fillcolor("yellow")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("cyan")
fillcolor("red")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("green")
fillcolor("cyan")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

seite = seite + aenderung
pencolor("yellow")
fillcolor("blue")
begin_fill()
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
forward(seite)
left(90)
end_fill()

right(60)

hideturtle()
