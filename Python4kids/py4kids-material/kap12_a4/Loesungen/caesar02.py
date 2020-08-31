# Python für Kids (4. Auflage) - Kapitel 12
# Wörterbücher, Dateien und der alte Cäsar

# Lösung zu Aufgabe 2

# Autor: Gregor Lingl
# Datum 12. 8. 2009

# caesar02.py  

def caesarcode(buchstabe):
    klar = "abcdefghijklmnopqrstuvwxyz"
    i = klar.index(buchstabe)
    geheim = klar[i:] + klar[:i]
    code = {}
    for j in range(len(klar)):
        code[klar[j]] = geheim[j]
    return code

def decodedict(codedict):
    dc = {}
    for schluessel, wert in codedict.items():
        dc[wert] = schluessel
    return dc

def codiere(text, codedict):
    text = text.lower()
    geheim = ""
    for b in text:
        if b in codedict:
            neu = codedict[b]
        else:
            neu = b
        geheim = geheim + neu
    return geheim

def codiere_datei(dateiname, char):
    try:
        f = open(dateiname + ".txt", "r")
        text = f.read()
        f.close()
    except:
        print("{0}: Lesen misslungen!".format(dateiname))
        return
    geheim = codiere(text, caesarcode(char))
    try:
        g = open(dateiname+".caes", "w")
        g.write(geheim)
        g.close()
    except:
        print("{0}: Schreiben misslungen!".format(dateiname))

def decodiere_datei(dateiname, char):
    try:
        f = open(dateiname + ".caes", "r")
        text = f.read()
        f.close()
    except:
        print("{0}: Lesen misslungen!".format(dateiname))
        return
    cc = caesarcode(char)
    dc = decodedict(cc)
    klar = codiere(text, dc)
    try:
        g = open(dateiname+"_dec.txt", "w")
        g.write(klar)
        g.close()
    except:
        print("{0}: Schreiben misslungen!".format(dateiname))

