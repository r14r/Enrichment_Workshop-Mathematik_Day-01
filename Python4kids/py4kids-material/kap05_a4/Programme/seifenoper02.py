# Python für Kids -- 4. Auflage, Kapitel 5
# Autor: Gregor Lingl
# Datum: 7. 8. 2009
# seifenoper02.py

def seifenoper(mann, frau, konkurrent, ereignis=""):
    print()
    print("{0} liebt {1}.".format(mann, frau))
    print("{1} findet {0} nicht besonders interessant.".format(mann, frau))
    print("{0} ist verrückt nach {1}.".format(frau, konkurrent))
    print("{0} mag {1} gar nicht!".format(mann, konkurrent))
    if ereignis != "":
        print("Da verändert {0} alles".format(ereignis), end="")
    print("...")
    print()

seifenoper( "Uwe", "Karin", "Kurt" )
seifenoper( "Fritz", "Mizzi", "Charly", "eine harmlose Einladung")

seifenoper( "Doris", "Paul", "Eva", "eine Krankheit" )
# hier ist:
#   mann ---> "Doris"
#   frau ---> "Paul"
#   rivale ---> "Eva"
#   ereignis ---> "eine Krankheit"
