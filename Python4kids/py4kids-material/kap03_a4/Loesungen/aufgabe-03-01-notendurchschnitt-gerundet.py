# Python für Kids -- 4. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# aufgabe-03-01.py - Kapitel 3,  Aufgabe 1 

print ("""
Notendurchschnittsberechnung:
=============================
""")
name = input("Name: ")
fach = input("Gegenstand: ")
print("Noten für")
note1 = input("  1. Klassenarbeit: ")
note2 = input("  2. Klassenarbeit: ")
note3 = input("  3. Klassenarbeit: ")
note1 = float(note1)
note2 = float(note2)
note3 = float(note3)
durchschnitt = (note1 + note2 + note3) / 3
durchschnitt = round(durchschnitt, 2)              # (1)
print("Der Notendurchschnitt von", name, end=" ")  # (2)
print("in", fach, "ist:", durchschnitt)

#(1)

## >>> help(round)
## Hilfe für die eingebaute Funktion round:
##
## round(...)
##     round(Zahl[, AnzahlZiffern]) -> Zahl
##    
##     Runde Zahl auf durch AnzahlZiffern gegebene Genauigkeit
##     (Voreinge Funktion mit einem Argument aufgerufen wird, 
##     gibt sie eine ganze Zahl (int) zurück, andernfalls ein
##     Zahl vom gleichen Typ wie die Eingabe Zahl.
##     Das optionale Argument AnzahlZiffern kann negativ sein.

# (2)

## mit dem (optionalen) Argument end=" " wird die Ausgabe der
## print() Funktion nicht mit einer neuen Zeile, sondern nur mit
## einem Leerzeichen ab geschlossen.
## Der nächste Aufruf der print() Funktion schreibt in der
## selben Zeile weiter.
