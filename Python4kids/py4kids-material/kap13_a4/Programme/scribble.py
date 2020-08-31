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
# (9) Farbwähler
# (10) Hilfebildschirm ein (F1) und aus (Escape)

# Bild als Postscript speichern und in png-Datei konvertieren
# Windows-Version
# benötigt Ghostscript

# scribble_undo hack, tracer(False) fur GUI-Aufbau,
# F1 - Hinweis im Titel

from turtle import Screen, Turtle
import sys
sys.setrecursionlimit(20000)

GHOSTSCRIPTFILE = "C:/Programme/gs/gs8.60/bin/gswin32c.exe "
SCREENBREITE = 800
SCREENHOEHE = 600
RAND = 40
WERKZEUGBREITE = WB = 35
LINKERRAND = - SCREENBREITE / 2 + 40

def save():
    import os
    filename = screen.textinput("Grafik speichern", "Dateiname:")
    screen.update()
    cv = screen.getcanvas()
    cv.postscript(file=filename+".ps", x=LINKERRAND)
    os.system( GHOSTSCRIPTFILE +
                      "-sDEVICE=png16m -o {0}.png {0}.ps".format(filename))
    screen.listen()

def waehlelinienfarbe():
    farbe = askcolor()
    stift.pencolor(farbe[1])

def waehlefuellfarbe():
    farbe = askcolor()[1]
    fuellanzeiger.fillcolor(farbe)
    if stift.filling():
        stift.fillcolor(farbe)   

def jump(x, y):
    if x < LINKERRAND: return
    stift.penup()
    stift.goto(x, y)
    stift.pendown()

def moveto(x, y):
    if x < LINKERRAND: return
    stift.goto(x,y)    

def fuellenumschalten(xdummy, ydummy):
    if xdummy < LINKERRAND: return
    if stift.filling():
        stift.end_fill()
        stift.fillcolor("")
    else:
        stift.begin_fill()
        stift.fillcolor(fuellanzeiger.fillcolor())

def scribble_undo():
    # the scribble_undo hack 
    stift.undo()
    if not stift.filling() and stift.fillcolor():
        stift.undo()
        stift.fillcolor("")
    
def farbButton(farbe, y):
    t = Turtle(visible=False)
    t.shape("square")
    t.speed(0)
    t.pu(); t.goto(LINKERRAND-20,y);
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

def show_help():
    screen.title("SCRIBBLE - Das Malprogramm")
    helper.stamp()
    helptext = """
                   SCRIBBLE - Hilfe

Maus-Kommandos für die Zeichenfläche:
-------------------------------------
Mausklick links -- zeichnet Linie zur Mausposition
Mausziehen links -- zeichnet Linie längs der Mausbewegung
Mausklick Mitte -- bewegt Stift zur Mausposition
Mausklick rechts -- schaltet Füllen ein bzw. aus

Maus-Kommandos für die Farb-Buttons:
------------------------------------
Mausklick links -- stellt Stiftfarbe ein
Mausklick rechts -- stellt Füllfarbe ein. Die Füllfarbe
                    wird unten im Füllfarbanzeiger angezeigt

Tastatur-Kommandos:
-------------------
"1" .. "9" -- stellt Strichdicke auf die Werte 1 .. 9
Backspace -- macht die letzten Zeichenvorgänge rückgängig
Leertaste -- löscht Zeichnung
"l" -- ruft Farbauswahldialog für die Linienfarbe auf
"f" -- ruft Farbauswahldialog für die Füllfarbe auf
"s" -- Speichert das gescribblete Bild als *.png-Datei
F1  -- ruft diese Hilfe auf
Escape -- schließt den Hilfe Bildschirm. 
"""
    helper.goto(0, -260)
    helper.write(helptext, align="center", font=("Courier", 14, "bold"))
    helper.home()


screen = Screen()
screen.clear()
screen.setup(SCREENBREITE+RAND, SCREENHOEHE+RAND)
screen.screensize(SCREENBREITE, SCREENHOEHE)
screen.title("SCRIBBLE - Das Malprogramm   (Hilfe: F1)")
screen.tracer(False)
stift = Turtle()
stift.speed(0)
stift.shape("circle")
stift.shapesize(0.4, 0.4, 3)
stift.pensize(3)

fuellanzeiger = Turtle(shape="circle")
fuellanzeiger.pu()
fuellanzeiger.speed(0)
fuellanzeiger.goto(LINKERRAND-20, -SCREENHOEHE / 2 + WERKZEUGBREITE)
fuellanzeiger.color("black", "")

helper = Turtle(shape="square", visible=False)
helper.pu()
helper.speed(0)
helper.fillcolor("white")
helper.shapesize(35,29,3)

screen.onclick(moveto)
screen.onclick(jump, 2)
screen.onclick(fuellenumschalten, 3)
stift.ondrag(moveto)

for (f,y) in (("red", 4*WB), ("green", 3*WB), ("blue", 2*WB),
              ("yellow", WB), ("cyan", 0), ("magenta", -WB),
              ("black", -2*WB), ("white", -3*WB)):
    farbButton(f, y)

screen.onkeypress(scribble_undo, "BackSpace")
for c in "123456789":
    def setpensize(ps=int(c)):
        stift.pensize(ps)
        stift.shapesize(0.2 + ps/10)
    screen.onkeypress(setpensize, c)
screen.onkeypress(stift.clear, "space")
screen.onkeypress(save, "s")
screen.onkeypress(waehlelinienfarbe, "l")
screen.onkeypress(waehlefuellfarbe, "f")
screen.onkeypress(show_help, "F1")
screen.onkeypress(helper.clear, "Escape")
screen.tracer(True)
screen.listen()

#screen.mainloop()
