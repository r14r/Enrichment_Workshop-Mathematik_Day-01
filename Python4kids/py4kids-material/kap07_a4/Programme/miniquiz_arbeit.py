# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 8. 8. 2009
# miniquiz_arbeit.py  - Umarbeitung

# (frage,loesung) – Tupel für das Quiz
# kann erweitert und/oder geändert werden 

quizdaten=(("Welche Programmiersprache lernst du " +
                                      "gerade? ", "Python"),
           ("Mit welchem reservierten Wort beginnen " + 
                         "Funktionsdefinitionen? ", "def"),
           ("Wie viele reservierte Wörter hat Python? ", "33"),
           ("Mit welchem reservierten Wort beginnen " +
                         "Zählschleifen? ", "for")
          )

def quizfrage(quizeintrag):
    global punkte
    frage, loesung = quizeintrag
    antwort = input(frage)
    if antwort == loesung:
        print("Richtig!")
        punkte = punkte + 1
    else:
        print("Leider falsch!")
        print("Richtig ist:", loesung)
    print()

print("""
Hallo! Du kannst hier ein paar Quizfragen
beantworten, um dein Wissen zu Überprüfen.""")
name = input("Wie heißt du denn? ")
print("Also viel Glück,", name, "- es geht los!")

punkte = 0

for eintrag in quizdaten:
    quizfrage(eintrag)

fragen_zahl = len(quizdaten)
print()
print("Du hast {0} von {1} Punkten erreicht!".format(punkte,
                                                fragen_zahl))

if punkte > fragen_zahl * 0.8:
    print("Super,",end=" ")
elif punkte > 0:
    print("Fein, du hast schon einiges gelernt,", end=" ")
else:
    print("Du stehst noch ziemlich am Anfang,", end=" ")
print("{0}!".format(name))
print()
print("Sieh dir doch mal das Python-Video auf der CD an!")
