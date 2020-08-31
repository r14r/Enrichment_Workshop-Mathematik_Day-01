# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# miniquiz04.py : Python für Kids, Kapitel 4
#                 Quiz aus drei Fragen.

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

print("Du hast", punkte, "von 3 Punkten erreicht!")
