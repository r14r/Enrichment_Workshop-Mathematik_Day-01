# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# seifenoper01.py

def seifenoper(mann, frau, konkurrent, ereignis=""):
    print(mann, "liebt", frau + ".")
    print(frau, "findet", mann, "nicht besonders interessant.")
    print(frau, "ist verrückt nach", konkurrent + ".")
    print(mann, "mag", konkurrent, "gar nicht!")
    if ereignis != "":
        print("Da verändert", ereignis, "alles", end="")
    print("...")
    print()

seifenoper( "Uwe", "Karin", "Kurt" )
#seifenoper( "Uwe", "Karin", "Kurt", "ein Unfall" )
