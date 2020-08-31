# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum: 11. 10. 2009
# Zwei Lösungen zu Aufgabe 1 aus Kapitel 11

def besprache(txt):
    betxt = ""
    for c in txt:
        if c.lower() in "aeiouäöü":
            betxt = betxt + (c + "b" + c.lower())
        else:
            betxt = betxt + c
    return betxt   

def besprache2(txt):
    return "".join(c + "b" + c.lower() if c.lower() in "aeiouäöü" else c
                   for c in txt)  # ein Generator-Ausdruck!

s = "Das ist witzig!"
print(s)
print(besprache(s))
print()
print(besprache2("Äolische Inseln"))
print()

s = "abarakadabara"
print(s, "==>", besprache2(s))



