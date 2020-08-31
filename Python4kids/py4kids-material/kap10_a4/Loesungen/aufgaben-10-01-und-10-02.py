# Python für Kids -- 4. Auflage, Kapitel 10
# Autor: Gregor Lingl
# Datum: 10. 8. 2009
# Lösungen zu den Aufgaben aus Kapitel 10

from math import sqrt

def hypotenuse(a, b):
    return sqrt(a**2 + b**2)

def fib1(n):
    a = b = 1
    while n > 1:
        a, b = b, a + b
        n = n - 1
    return a


def fib2(n):
    """Wie fib1(n), aber in 'traditioneller' Formulierung:
    """
    a = 1
    b = 1
    for f in range(3, n+1):
        tmp = a + b
        a = b
        b = tmp
    return b


def fib(n):
    """Wie fib2(n), aber mehr 'pythonesk':
    """
    a = b = 1
    for f in range(n-2):
        a, b = b, a + b
    return b
