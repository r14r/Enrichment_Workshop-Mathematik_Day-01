# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 8. 8. 2009
# miniquiz_arbeit.py  - Umarbeitung

def quizfrage():
    global punkte
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

frage = "Welche Programmiersprache lernst du gerade? "
loesung = "Python"
quizfrage()

frage = """Mit welchem reservierten Wort beginnt eine
Funktionsdefinition? """
loesung = "def"
quizfrage()

frage = "Wieviel reservierte Wörter hat Python? "
loesung = "33"
quizfrage()

print()
print("Du hast", punkte, "von 3 Punkten erreicht!")

if punkte == 3:
    print("Super,",end=" ")
elif punkte > 0:
    print("Fein, du hast schon einiges gelernt,", end=" ")
else:
    print("Du stehst noch ziemlich am Anfang,", end=" ")
print(name, "!")
print()
print("Sieh dir doch mal das Python-Video auf der CD an!")
