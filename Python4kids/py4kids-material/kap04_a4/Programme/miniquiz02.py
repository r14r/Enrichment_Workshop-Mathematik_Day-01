# Python für Kids -- 4. Auflage, Kapitel 4
# Autor: Gregor Lingl
# Datum: 6. 8. 2009
# miniquiz02.py : (2) - mit einer Verzweigung

frage = "Welche Programmiersprache lernst du gerade? "
loesung = "Python"

antwort = input(frage)
if antwort == loesung:
    print("Richtig!")
else:
    print("Leider falsch!")
    print("Richtig ist:", loesung)
