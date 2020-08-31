# Python für Kids -- 4. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 5. 8. 2008
# dreieck_06.py:  3 gleichseitige farbige, gefüllte Dreiecke

from turtle import *

reset()                        # leere Zeichenfläche herstellen
pensize(10)                    # Strichdicke 10 Pixel einstellen
right(90)                      # turtle in Ausgangsrichtung drehen

seite = 100    # <=== ein Name!

pencolor("red")
fillcolor("cyan")
begin_fill()
forward(seite)
left(120)
forward(seite)
left(120)
forward(seite)
left(120)
end_fill()

left(120)

seite = 135  
pencolor("green")
fillcolor("magenta")
begin_fill()
forward(seite)
left(120)
forward(seite)
left(120)
forward(seite)
left(120)
end_fill()

left(120)

seite = 65   
pencolor("blue")
fillcolor("yellow")
begin_fill()
forward(seite)
left(120)
forward(seite)
left(120)
forward(seite)
left(120)
end_fill()

left(120)
