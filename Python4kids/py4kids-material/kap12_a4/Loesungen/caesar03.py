# Python für Kids (4. Auflage) - Kapitel 12
# Wörterbücher, Dateien und der alte Cäsar

# Lösung zu Aufgabe 3

# Autor: Gregor Lingl
# Datum 12. 8. 2009
# caesar03.py  

TESTTEXT = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

KLAR = "abcdefghijklmnopqrstuvwxyz"

def caesarcode(buchstabe):
    i = KLAR.index(buchstabe)
    geheim = KLAR[i:] + KLAR[:i]
    return dict(zip(KLAR, geheim))

def codiere(text, buchstabe):
    text = text.lower()
    cc = caesarcode(buchstabe)
    geheim = ""
    for b in text:
        geheim = geheim + cc.get(b, b)
    return geheim

def decodiere(geheim, buchstabe):
    b = KLAR[-KLAR.index(buchstabe)]
    return codiere(geheim, b)

def codiere_datei(dateiname, char):
    f = open(dateiname + ".txt")
    text = f.read()
    f.close()
    geheim = codiere(text, char)
    g = open(dateiname+".caes", "w")
    g.write(geheim)
    g.close()

def decodiere_datei(dateiname, char):
    f = open(dateiname + ".caes")
    text = f.read()
    f.close()
    klar = decodiere(text, char)
    g = open(dateiname+"_decodiert.txt", "w")
    g.write(klar)
    g.close()


