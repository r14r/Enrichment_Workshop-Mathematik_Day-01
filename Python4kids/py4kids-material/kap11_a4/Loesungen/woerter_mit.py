# Python für Kids - 4. Auflage

# Autor: Gregor Lingl
# Datum: 11. 10. 2009
# Lösung zu Aufgabe 2 aus Kapitel 11

txt = """Erstelle eine Funktion, die aus einem String,
der einen längeren Text enthält, eine Liste jener Wörter
erzeugt, die einen bestimmten Buchstaben enthalten."""

def woerter_mit(t, c):
    return [x for x in t.split() if c.lower() in x.lower()]

print()
print(txt)
print()
print("Wörter mit s:", *woerter_mit(txt, "s"))
print("Wörter mit st:", *woerter_mit(txt, "st"))
print("Wörter mit ist:", *woerter_mit(txt, "ist"))

