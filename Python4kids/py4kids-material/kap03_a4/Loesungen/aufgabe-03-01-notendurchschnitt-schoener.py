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
durchschnitt = round(durchschnitt, 2)
# Mehrere Argumente innerhalb einer runden Klammer
# müssen nicht in einer Zeile stehen!
print("Der Notendurchschnitt von", name,
      "in", fach, "ist:", durchschnitt)
