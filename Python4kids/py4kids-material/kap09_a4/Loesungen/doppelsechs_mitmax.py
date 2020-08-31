# Python für Kids -- 4. Auflage, Kapitel 9
# Autor: Gregor Lingl
# Datum: 10. 8. 2009

## Zu Kapitel 9, Aufgabe 3b
## Zwei AUFEINANDERFOGENDE Sechser Würfeln
## mit Ermittlung der längsten Wurffolge

## mit einigen Sprachelementen, die du noch nicht kennst!
## Findest du passende Infos in der Python-Dokumentation (F1)?
## Suche nach der eingebauten Funktion max()

from random import randint

wurfsumme = 0
anzahl_spiele = 10000
maxlaenge = 2

for i in range(anzahl_spiele):
    # Ein Spiel
    wurf1 = randint(1,6)
    wurf2 = randint(1,6)    
    wuerfe = 2
    while not wurf1 == wurf2 == 6:
        wurf1, wurf2 = wurf2, randint(1,6)
        wuerfe += 1
    # Das Spiel ist aus
    maxlaenge = max(wuerfe, maxlaenge)
    wurfsumme = wurfsumme + wuerfe
    
print()
print("Versuchsreihe mit", anzahl_spiele, "Spielen:")
print("Durchschnitt für zwei Sechser hintereinander:", end=" ")
print(wurfsumme / anzahl_spiele)
print()
print("Größte Wurffolgenlänge:", maxlaenge)
print()
input("Beenden mit Eingabetaste!")


