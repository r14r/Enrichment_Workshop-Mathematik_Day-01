# Python für Kids (4. Auflage) - Kapitel 11
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum 11. 8. 2009

# frang_generator.py  

def frange(start, stop, schritt=1):
    """ein Generator von floating point Zahlen
    von start bis stop mit Schrittweite step."""
    element = float(start)  # macht aus start ein Kommazahl
    yield element
    while element < stop:
        element = element + schritt
        yield element
    
