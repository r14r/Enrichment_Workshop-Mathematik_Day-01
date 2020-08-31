### Python für Kids - Kapitel 14 ###
# Autor: Gregor Lingl
# Datum: 20. 8. 2009
#
# Lösung zur Übungsaufgabe, Teil (a)

class Bankkonto:
    def __init__(self, einlage = 0):
        self.kontostand = einlage
    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag
    def abheben(self, betrag):
        self.kontostand = self.kontostand - betrag
    def kontostand_abfrage(self):
        print(self.kontostand)

annas_konto = Bankkonto(950.0)
bertas_konto = Bankkonto(105)

print("Anna:", end=" ")
annas_konto.kontostand_abfrage()
print ("Berta:", end=" ")
bertas_konto.kontostand_abfrage()

annas_konto.einzahlen(233.25)
bertas_konto.abheben(124.36)

print("Anna:", end=" ")
annas_konto.kontostand_abfrage()
print("Berta:", end=" ")
bertas_konto.kontostand_abfrage()


        
