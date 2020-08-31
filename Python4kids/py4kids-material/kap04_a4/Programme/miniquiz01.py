# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# miniquiz01.py : (1) - mit 2 bedingten Anweisungen

frage = "Welche Programmiersprache lernst du gerade? "
loesung = "Python"

antwort = input(frage)
if antwort == loesung:
    print("Richtig!")
if antwort != loesung:
    print("Leider falsch!")
    print("Richtig ist:", loesung)
