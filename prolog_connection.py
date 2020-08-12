from pyswip import Prolog
import main as plato

prolog = Prolog()
prolog.consult("Hechos.pl")
plato.plato_ingrediente(prolog)
plato.plato_procedimiento(prolog)
plato.plato_ingrediente_lista(prolog)

Q1= input("\n¿Qué plato puedo preparar con el ingrediente...?")

valorfinal = list(prolog.query("buscar_ingrediente(%s ,Y)" % Q1.lower()))
for valor in valorfinal:
    print(Q1, "==>", valor["Y"])

#Q2 function
print("\n**¿Cuáles platos se pueden preparar si tengo 3 ingredientes específicos?**\n")
Q2_1= input("Ingrediente 1:\n")
Q2_2=input("Ingrediente 2:\n")
Q2_3=input("Ingrediente 2:\n")

valorfinalQ2 = list(prolog.query("ingredientes_especificos(%s, %s, %s ,Y)" % (Q2_1.lower(), Q2_2.lower(), Q2_3.lower())))
for valorQ2 in valorfinalQ2:
    print(Q2_1, Q2_2, Q2_3, "==>", valorQ2["Y"])

#Q3

print("\n**¿Cuáles platos implican usar la batidora (ej.: Batir la masa) como procedimiento?**\n")

batidora_procedimiento = "batir la masa".replace(" ", "_")
valorfinalQ3 = list(prolog.query("plato_procedimiento(Plato, %s)" % batidora_procedimiento))

for valorQ3 in valorfinalQ3:
    print(valorQ3["Plato"])

#Q4

print("\n**¿Cuáles platos implican usar la batidora (ej.: Batir la masa) como procedimiento?**\n")
ingrediente_batidora = "batidora"
valorfinalQ4 = list(prolog.query("noIngrediente(%s, Plato)" % ingrediente_batidora))

