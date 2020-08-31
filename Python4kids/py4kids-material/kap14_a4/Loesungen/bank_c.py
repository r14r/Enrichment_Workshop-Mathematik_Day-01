### Python für Kids - 4. Auflage - Kapitel 14 ###
# Autor: Gregor Lingl
# Datum: 20. 8. 2009
#
# Lösung zur Übungsaufgabe, Teil (c)

# Das Bankkonto gibt seinen Kontostand zwar aus,
# überlässt das printen aber z. B. einem Bankomat

class Bankkonto:
    def __init__(self, einlage = 0):
        self.kontostand = einlage
    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag
    def abheben(self, betrag):
        self.kontostand = self.kontostand - betrag
    def kontostand_abfrage(self):
        return self.kontostand
    def ueberweisen(self, betrag, konto):
        self.abheben(betrag)
        konto.einzahlen(betrag)
        
annas_konto = Bankkonto(950.0)
bertas_konto = Bankkonto(105)

print("Anna:", annas_konto.kontostand_abfrage())
print ("Berta:", bertas_konto.kontostand_abfrage())

annas_konto.einzahlen(233.25)
bertas_konto.abheben(124.36)

print("Anna:", annas_konto.kontostand_abfrage())
print("Berta:", bertas_konto.kontostand_abfrage())

# Anna überweist an Berta 498.0 Euro:
annas_konto.ueberweisen(498.0, bertas_konto)

print("Anna:", annas_konto.kontostand_abfrage())
print("Berta:", bertas_konto.kontostand_abfrage())

        
