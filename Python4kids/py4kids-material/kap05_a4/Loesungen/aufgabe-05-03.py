# Python für Kids -- 4. Auflage, Kapitel 5

# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# Loesung von Kapitel 5, Aufgabe 3: 

def zahlwort(zahl):
    einer = zahl % 10  # Einerstelle: Rest bei der Division von zahl durch 10
    if einer == 1: e = "ein"
    elif einer == 2: e = "zwei"
    elif einer == 3: e = "drei"
    elif einer == 4: e = "vier"
    elif einer == 5: e = "fünf"
    elif einer == 6: e = "sechs"
    elif einer == 7: e = "sieben"
    elif einer == 8: e = "acht"
    elif einer == 9: e = "neun"

    zehner = zahl // 10  # Zehnerstelle: Ergebnis der Ganzzahldivision
                         # von zahl durch 10
    if zehner == 0:   z = ""
    elif zehner == 1: z = "zehn"
    elif zehner == 2: z = "zwanzig"
    elif zehner == 3: z = "dreissig"
    elif zehner == 4: z = "vierzig"
    elif zehner == 5: z = "fünfzig"
    elif zehner == 6: z = "sechzig"
    elif zehner == 7: z = "siebzig"
    elif zehner == 8: z = "achtzig"
    elif zehner == 9: z ="neunzig"

    if zahl == 11:    print("elf")
    elif zahl == 12:  print("zwölf")
    elif zahl == 17:  print("siebzehn")
    elif einer == 0:  print(z)
    elif zehner == 1: print(e+z)
    else:             print(e+"und"+z)

zahl = input("Gib eine zweistellige ganze Zahl ein: ")
zahl = int(zahl)  # macht aus dem String zahl eine ganze Zahl
zahlwort(zahl)

## Wenn du die folgenden drei Zahlen entkommentierst, erhältst
## du die Zahlwörter von zehn bis neunundneunzig

for i in range(10,100):
    print(i, end=" ")
    zahlwort(i)

    
    
