# Python für Kids -- 4. Auflage, Kapitel 3
# Autor: Gregor Lingl
# Datum: 5. 8. 2009
# dialog02.py : Eingabedialog mit Taschengeldberechnung

print("Hallo! Schönen Tag heute!")
name = input("Wie heißt du? ")
print("Fein, dich hier zu sehen,", name)
geld = input("Wie viel Euro Taschengeld bekommst du monatlich? ")
geld = float(geld)
geldProJahr = geld * 12
print("Wow! Das sind ja", geldProJahr, "€ im Jahr!")                 
