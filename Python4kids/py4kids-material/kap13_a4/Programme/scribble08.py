# Python für Kids (4. Auflage) - Kapitel 13
# Ereignisgesteuerte Programme

# Autor: Gregor Lingl
# Datum 16. 8. 2009

# scribble - ein einfaches Zeichenprogramm

# (1) Stift zeichnet eine Linie zur (links) angeklickten Stelle
# (2) Stift springt (ohne Zeichnen) zur mit mittlerer Taste
#     angeklickten Stelle
# (3) Stift kritzelt, wenn er gezogen wird
# (4) rechte Maustaste schaltet füllen ein und aus
# (5) undo() - Funktion des Stiftes an BackSpace-Taste binden
#     clear() - Funktion des Stiftes an die Leertaste binden
# (6) Strichdicken 1..9 an Tasten "1" .. "9" binden
# (7) Farbknöpfe:
#     - mit linker Maustaste anklicken: Zeichenfarbe
#     - mit rechter Maustaste anklicken: Füllfarbe
# (8) Füllfarbanzeiger

from turtle import Screen, Turtle
import sys 
sys.setrecursionlimit(20000)

def jump(x, y):
    if x < -360: return
    stift.penup()
    stift.goto(x, y)
    stift.pendown()

def moveto(x, y):
    if x < -360: return
    stift.goto(x,y)    

def fuellenumschalten(xdummy, ydummy):
    if xdummy < -360: return
    if stift.filling():
        stift.end_fill()
        stift.fillcolor("")
    else:
        stift.begin_fill()
        stift.fillcolor(fuellanzeiger.fillcolor())

def farbButton(farbe, y):
    t = Turtle(visible=False)
    t.shape("square")
    t.speed(0)
    t.pu(); t.goto(-380,y);
    t.fillcolor(farbe)
    def setpencolor(xdummy, ydummy, c=farbe):
        stift.pencolor(c)
    def setfillcolor(xdummy, ydummy, c=farbe):
        fuellanzeiger.fillcolor(c)
        if stift.filling():
            stift.fillcolor(c)
    t.onclick(setpencolor)
    t.onclick(setfillcolor, 3)
    t.showturtle()

screen = Screen()
screen.clear()
screen.setup(840, 600)
screen.title("SCRIBBLE - Das Malprogramm")
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)

fuellanzeiger = Turtle(shape="circle")
fuellanzeiger.pu()
fuellanzeiger.speed(0)
fuellanzeiger.goto(-380, -240)
fuellanzeiger.color("black", "")

screen.onclick(moveto)
screen.onclick(jump, 2)
screen.onclick(fuellenumschalten, 3)
stift.ondrag(moveto)

for (f,y) in (("red", 160), ("green", 120), ("blue", 80),
              ("yellow", 40), ("cyan", 0), ("magenta", -40),
              ("black", -80), ("white", -120)):
    farbButton(f, y)

screen.onkeypress(stift.undo, "BackSpace")
for c in "123456789":
    def setpensize(ps=int(c)):
        stift.pensize(ps)
        stift.shapesize(0.1 + ps/10)
    screen.onkeypress(setpensize, c)
screen.onkeypress(stift.clear, "space")
screen.listen()
