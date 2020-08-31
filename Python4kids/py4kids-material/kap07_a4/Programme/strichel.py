# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# strichel.py  -- zeichne eine strichlierte Linie

from turtle import *
from mytools import jump

def strichel(laenge, striche=10):
    spruenge = striche - 1
    strich = laenge / (striche + spruenge)
    for i in range(spruenge):
        forward(strich)
        jump(strich)
    forward(strich)
