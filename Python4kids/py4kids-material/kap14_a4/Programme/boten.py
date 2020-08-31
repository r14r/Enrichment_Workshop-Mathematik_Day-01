# Python für Kids - 4. Auflage - Kapitel 14 ###
# Autor: Gregor Lingl
# Datum: 20. 08. 2009
#
# boten.py (Kap. 14)
#

class Bote1:
    def melde(self):
        print("Ich melde dir:", "Hallo!")

class Bote2:
    def melde(self, text):
        print("Ich melde dir:", text)

##class SchlauerBote:
##    def merke(self, text):
##      self.botschaft = text
##    def melde(self):
##      print("Ich melde dir:", self.botschaft)

# Fassung mit Konstruktor:

class SchlauerBote:
    def __init__(self):
        self.botschaft = "Hi!"
    def merke(self, text):
        self.botschaft = text
    def melde(self):
        print("Ich melde dir:", self.botschaft)

class SehrSchlauerBote(SchlauerBote):
    def merke_dazu(self, zusatz):
        self.botschaft = self.botschaft+zusatz

class FreundlicherBote(SchlauerBote):
    def __init__(self, grusstext):
        SchlauerBote.__init__(self)
        self.gruss = grusstext
    def gruesse(self):
        print self.gruss
    def melde(self):
        self.gruesse()
        SchlauerBote.melde(self)

class Agent(SchlauerBote):
    def weitersagen(self, agent):
        agent.merke(self.botschaft)
    def belausche(self, agent):
        self.botschaft = agent.botschaft
        
