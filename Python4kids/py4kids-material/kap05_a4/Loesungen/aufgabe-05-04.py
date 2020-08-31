# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# Loesung von Kapitel 5, Aufgabe 4: 

def gruss(anrede, ort, beschreibung1, tun, beschreibung2, absender):
    print(anrede+"!")
    print("Hier in "+ort+" gefällt es mir "+beschreibung1+".")
    print("Gestern waren wir "+tun+". Das war "+beschreibung2+"!")
    print("Bis bald!")
    print(absender)

gruss("Lieber Buffi", "Rhodos", "sehr, sehr gut",
      "schwimmen", "traumhaft", "Deine Clara-Pythia")

