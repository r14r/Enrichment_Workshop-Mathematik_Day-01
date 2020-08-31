# Python für Kids (4. Auflage) - Kapitel 11
# Objekte und Methoden

# Autor: Gregor Lingl
# Datum 11. 8. 2009

# listenzeug.py  

def krange(start, stop, schritt=1):
    """erzeugt Liste von floating point Zahlen
    von start bis stop mit Schrittweite step."""
    zahlenliste = []
    element = float(start)  # macht aus start ein Kommazahl
    while element < stop:
        zahlenliste.append(element)
        element = element + schritt
    return zahlenliste

def frange(start, stop, schritt=1):
    """ein Generator von floating point Zahlen
    von start bis stop mit Schrittweite step."""
    element = float(start)  # macht aus start ein Kommazahl
    while element < stop:
        yield element
        element = element + schritt

    
