# Python für Kids -- 4. Auflage, Kapitel 2
# Autor: Gregor Lingl
# Datum: 5. 8. 2008
# dreieck01.py:  gleichseitiges farbiges, gefülltes Dreieck

from turtle import *

reset()            # leere Zeichenfläche herstellen
pensize(10)        # Strichdicke 10 Pixel einstellen
right(90)          # turtle in Ausgangsrichtung drehen

pencolor("red")
fillcolor("cyan")
begin_fill()
forward(135)
left(120)
forward(135)
left(120)
forward(135)
left(120)
end_fill()
