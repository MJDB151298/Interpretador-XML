:- dynamic plato_ingrediente/2.

buscar_ingrediente(P, I):- plato_ingrediente(I, P).
ingredientes_especificos(Ing1, Ing2, Ing3, Plato):- plato_ingrediente(Plato, Ing1), plato_ingrediente(Plato, Ing2), plato_ingrediente(Plato, Ing3).
