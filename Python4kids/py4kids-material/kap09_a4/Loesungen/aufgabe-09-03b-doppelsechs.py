# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
## Lösung von Kapitel 9 - Aufgabe 3b
## Zwei AUFEINANDERFOGENDE Sechser Würfeln

from random import randint

wurfsumme = 0
anzahl_spiele = 20000

for i in range(anzahl_spiele):
    # Ein Spiel
    wurf1 = randint(1,6)
    wurf2 = randint(1,6)    
    wuerfe = 2
    while not wurf1 == wurf2 == 6:
        wurf1 = wurf2
        wurf2 = randint(1,6)
        wuerfe = wuerfe + 1
    # Das Spiel ist aus
    wurfsumme = wurfsumme + wuerfe
    
print()
print("Versuchsreihe mit", anzahl_spiele, "Spielen:")
print("Durchschnitt für zwei Sechser hintereinander:", end=" ")
print(wurfsumme / anzahl_spiele)
print()
input("Beenden mit Eingabetaste!")
