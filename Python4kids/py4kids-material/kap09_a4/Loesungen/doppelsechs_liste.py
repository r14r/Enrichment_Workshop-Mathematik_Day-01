# Python für Kids -- 4. Auflage, Kapitel 9

# Autor: Gregor Lingl
# Datum: 10. 8. 2009

## Zu Kapitel 9, Aufgabe 3b
## Zwei AUFEINANDERFOGENDE Sechser Würfeln

## mit einigen Sprachelementen, die du noch nicht kennst!
## Findest du passende Infos in der Python-Dokumentation (F1)?
## Oder im Buch (Kapitel 11)?

from random import randint

wurfsumme = 0
anzahl_spiele = 10000

for i in range(anzahl_spiele):
    # Ein Spiel
    wuerfe = [randint(1,6), randint(1,6)]    
    while not wuerfe[-2] == wuerfe[-1] == 6:
        wuerfe.append(randint(1,6))
    # Das Spiel ist aus
    wurfsumme += len(wuerfe)
    
print()
print("Versuchsreihe mit", anzahl_spiele, "Spielen:")
print("Durchschnitt für zwei Sechser hintereinander:", end=" ")
print(wurfsumme / anzahl_spiele)
print()
input("Beenden mit Eingabetaste!")
