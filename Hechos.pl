:- dynamic plato_ingrediente/2.
:- dynamic receta_ingredientes_lista/2

existe(X,[X|_]).
existe(X,[_|Cola]):-existe(X,Cola).

buscar_ingrediente(P, I):- plato_ingrediente(I, P).
ingredientes_especificos(Ing1, Ing2, Ing3, Plato):- plato_ingrediente(Plato, Ing1), plato_ingrediente(Plato, Ing2), plato_ingrediente(Plato, Ing3).

noIngrediente(Ingrediente,Plato) :- plato_ingrediente(Plato,L), not(existe(Ingrediente,L)).

noIngredientes(Ing1, Ing2, Plato): noIngrediente(Ing1, Plato), noIngrediente(Ing2, Plato)