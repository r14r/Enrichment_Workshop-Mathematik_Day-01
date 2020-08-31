# Python für Kids (4. Auflage) - Kapitel 12
# Wörterbücher, Dateien und der alte Cäsar

# Autor: Gregor Lingl
# Datum 12. 8. 2009

# caesar01.py  -  Codieren/decodieren von Text mit dem Caesar-Code

testtext = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""


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
    for b in text.lower():
        if b in codedict:
            neu = codedict[b]
        else:
            neu = b
        geheim = geheim + neu
    return geheim

if __name__ == "__main__":
    print("Testtext:")
    print(testtext)
    print()

    cc = caesarcode("g")
    geheimtext = codiere(testtext, cc)

    print("Geheimtext:")
    print(geheimtext)
    print()

    dc = decodedict(cc)
    klartext = codiere(geheimtext, dc)

    print("Klartext:")
    print(klartext)

