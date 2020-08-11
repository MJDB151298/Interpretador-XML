from pyswip import Prolog

prolog = Prolog()
prolog.consult("Hechos.pl")

X = input("¿Qué plato puedo preparar con el ingrediente...?")

for valor in prolog.query("plato_ingrediente(" + X + ", Y)"):
    print(X, "==>", valor["Y"])


#Another Example
#for valor in prolog.query("le_gusta(X, Y)"):
 #   print("Le gusta", valor["X"], "esta cosa:", valor["Y"])