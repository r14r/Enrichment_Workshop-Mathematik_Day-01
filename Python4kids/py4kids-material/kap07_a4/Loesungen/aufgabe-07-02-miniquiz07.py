# Python für Kids -- 4. Auflage, Kapitel 7
# Autor: Gregor Lingl
# Datum: 8. 8. 2009

# miniquiz07.py

# (frage,loesung) – Tupel für das Quiz
# kann erweitert und/oder geändert werden 

pythonquiz=(("Welche Programmiersprache lernst du gerade? ",
              "Python"),
             ("Mit welchem reservierten Wort beginnt eine" +
              " Funktionsdefinition? ", "def"),
             ("Wieviel reservierte Wörter hat Python? ", "33"),
             ("Mit welchem reservierten Wort beginnen Zählschleifen? ",
              "for"),
             ("Wie heißt das Turtlegrafik-Modul, " +
               "mit dem du arbeitest? ", "turtle")
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

def quiz(quizdaten):
    global punkte
    print("""
Hallo! Du kannst hier ein paar Quizfragen
beantworten, um dein Wissen zu überprüfen.
""")
    name = input("Wie heißt du denn? ")
    print("Also viel Glück,", name, "- es geht los!")
    print()
    punkte = 0
    fragen_zahl = len(quizdaten)

    for eintrag in quizdaten:
        quizfrage(eintrag)

    print()
    print("Du hast", punkte, "von", fragen_zahl, "Punkten erreicht!")

    if punkte > fragen_zahl * 0.8:
        print("Super!")
    elif punkte >= fragen_zahl * 0.25:
        print("Fein, du hast schon einiges gelernt!")
    else:
        print("Du stehst noch ziemlich am Anfang!")

    print()
    print("Sieh dir doch mal das Python-Video auf der CD an!")

quiz(pythonquiz)
