:- dynamic plato_ingrediente/2.
:- dynamic receta_ingredientes_lista/2.

existe(X,[X|_]).
existe(X,[_|Cola]):-existe(X,Cola).

%Question1

buscar_ingrediente(P, I):- plato_ingrediente(I, P).

%Question2
ingredientes_especificos(Ing1, Ing2, Ing3, Plato):- plato_ingrediente(Plato, Ing1), plato_ingrediente(Plato, Ing2), plato_ingrediente(Plato, Ing3).

%Question4And5
noIngrediente(Ingrediente,Plato) :- receta_ingredientes_lista(Plato,L), not(existe(Ingrediente,L)).

%Question6
noIngredientes(Ing1, Ing2, Plato):- noIngrediente(Ing1, Plato), noIngrediente(Ing2, Plato).