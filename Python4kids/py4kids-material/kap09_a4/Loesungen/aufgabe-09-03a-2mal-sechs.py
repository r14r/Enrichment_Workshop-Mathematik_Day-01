# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
## Lösung von Kapitel 9 - Aufgabe 3a
## Zwei Sechser Würfeln  (oder zwei Sechsen?)

from random import randint

wurfsumme = 0
anzahl_spiele = 100000

for i in range(anzahl_spiele):
    # Ein Spiel
    sechser = 0
    wuerfe = 0
    while sechser < 2:
        wurf = randint(1,6)
        wuerfe = wuerfe + 1
        if wurf == 6:
            sechser = sechser + 1
    # Das Spiel ist aus
    wurfsumme = wurfsumme + wuerfe   

print()
print("Versuchsreihe mit", anzahl_spiele, "Spielen:")
print("Durchschnitt für zwei Sechser:", wurfsumme / anzahl_spiele)
print()
input("Beenden mit Eingabetaste!")
