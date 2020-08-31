# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# dreieck_arbeit_.py
# Zum Einstieg in 'Schleifen, die zählen'.


from turtle import *

def dreieck(laenge, farbe):
    """Zeichne Dreieck mit Seitenlänge laenge.
    Dreieckseiten werden in farbe gezeichnet.
    """
    pencolor(farbe)
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)

reset()
pensize(10)

dreieck(65, "red")
left(120)
   
dreieck(100, "green")
left(120)

dreieck(135, "blue")
left(120)

hideturtle()
