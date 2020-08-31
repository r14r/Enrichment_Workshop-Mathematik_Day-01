# Python für Kids -- 4. Auflage, Kapitel 5

# Politiker-Phrasengenerator
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# Lösung von Kapitel 5, Aufgabe 2: 

from random import choice

subjekt = """DER UNBEDINGTE WILLE
DAS ERKLÄRTE ZIEL
DIE SELBSTVERSTÄNDLICHE PFLICHT
DIE GESCHICHTLICHE AUFGABE
DIE UNERWARTETE GNADE
DIE TIEFE EINSICHT
DIE EINFACHE ABSICHT
DIE SCHLICHTE NOTWENDIGKEIT
DIE EINDEUTIGE ERKENNTNIS
DIE HOHE AMTSPFLICHT"""

weise = """HIER UND JETZT
IN ALLER OFFENHEIT
IN GEMEINSAMER ANSTRENGUNG
ZWISCHEN GESTERN UND MORGEN
OHNE "WENN" UND "ABER"
NOTFALLS IM ALLEINGANG
GEGEN ALLE WIDERSTÄNDE
GANZ UNMISSVERSTÄNDLICH
IN GUT UND BÖSE
AUCH GEGEN DEN ZEITGEIST"""

ziel = """MITEINANDER ZU REDEN
KRAFTVOLL ANZUPACKEN
NACH VORNE ZU BLICKEN
DIE KONTINUITÄT ZU WAHREN
GANZ BEWUSST ÖSTERREICHISCH ZU SEIN
DAS ZIEL ANZUSTREBEN
LETZTLICH ALLEIN ZU SEIN
DAS ICH VOR DAS WIR ZU STELLEN
DEM VATERLAND ZU DIENEN
GANZ EINFACH OBEN ZU BLEIBEN"""  ## EVENTUELL ÖSTERREICHISCH
                                 ## DURCH DEUTSCH ERSETZEN!

aufforderung = """IST DAS GEBOT DER STUNDE!
IST DIE GROSSE AUFGABE DER GEGENWART!
IST NUN EINE OBJEKTIVE NOTWENDIGKEIT!"""

def sprich():
    s = subjekt.splitlines()
    w = weise.splitlines()
    z = ziel.splitlines()
    a = aufforderung.splitlines()
    s = choice(s)
    w = choice(w)
    z = choice(z)
    a = choice(a)
    print("{}, {} {}, {}".format(s,w,z,a)) # Auto-Nummerierung
                                           # NEU in Python 3.1

sprich()
