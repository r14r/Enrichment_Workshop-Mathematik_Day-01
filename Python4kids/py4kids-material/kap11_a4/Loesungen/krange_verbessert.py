# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum: 11. 10. 2009
# Lösung zu Aufgabe 3 aus Kapitel 11

def krange(start, stop, schritt=1):
    """erzeugt Liste von floating point Zahlen
    von start bis stop mit Schrittweite step."""
##    if (stop - start) * schritt <= 0:
##        return []
    zahlenliste = []
    element = float(start)  # macht aus start ein Kommazahl
    ##### EIN kleiner TRICK:
    #
    # Wenn anfangs stop > element ist, d.h. stop - element > 0 ist,
    # dann muss auch schritt > 0 sein. 
    # Somit ist (stop-element)*schritt > 0 solange stop > element ist.
    #
    # Wenn anfangs stop < element ist, d.h. stop - element < 0 ist,
    # dann muss auch schritt < 0 sein. 
    # Somit ist ebenfalls (stop-element)*schritt > 0 solange stop < element ist.
    #
    ########################
    while (stop - element) * schritt > 0:  
        zahlenliste.append(element)
        element = element + schritt
    return zahlenliste

print(krange(-1000, +1000, +663.75))
print(krange(-1000, +1000, -663.75))
print(krange(+1000, -1000, -663.75))
print(krange(+1000, -1000, +663.75))
print()
print(krange(7/4, 1/2, -3/8))
print(krange(3/4, -1/2, -3/8))


