# Python für Kids -- 4. Auflage, Kapitel 10
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# quadrat.py : Übung für Kapitel 10

from math import sqrt

def quadrat(x):
    qu = x * x
    return qu

print(24, "zum Quadrat ist", quadrat(24))
b = 7
print(b, "zum Quadrat ist", quadrat(b))
cquadrat = quadrat(24) + quadrat(b)
print("{0}² + {1}² = {2}".format(24, b, cquadrat))


