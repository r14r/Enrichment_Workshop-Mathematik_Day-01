# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum 5. 8. 2009
# radioaktiv.py : Kapitel 2, Aufgabe 4 : Radioaktivitäts-Warnzeichen

from turtle import *

# QUADRAT

# zum Startpunkt
reset()

penup()
forward(100)
left(90)
forward(100)
left(90)
pendown()

pensize(5)
fillcolor("yellow")
# Quadrat zeichnen

begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

# zurück zum Ursprung

penup()
forward(100)
left(90)
forward(100)
pendown()

# drei schwarze Sektoren zeichnen

fillcolor("black")

begin_fill()
forward(80)
left(90)
circle(80,60)
left(90)
forward(80)
left(120)
end_fill()

left(120)

begin_fill()
forward(80)
left(90)
circle(80,60)
left(90)
forward(80)
left(120)
end_fill()

left(120)

begin_fill()
forward(80)
left(90)
circle(80,60)
left(90)
forward(80)
left(120)
end_fill()

left(120)

# Zentraler Kreis
penup()
forward(25)
left(90)
pencolor("yellow")
pendown()

begin_fill()
circle(25)
end_fill()

hideturtle()



