# Python für Kids (4. Auflage) - Kapitel 10
# Funktionen mit Wert
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# laufzeit.py : Laufzeitmessung

from time import clock

def laufzeit(anzahl, funktion, argument):
    anfang = clock()
    for i in range(anzahl):   
        funktion(argument)  
    ende = clock()
    return ende - anfang
