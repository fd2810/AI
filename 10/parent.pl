male(john).
male(mike).
male(david).

female(susan).
female(lisa).
female(anna).

parent(john, mike).
parent(susan, mike).

parent(john, lisa).
parent(susan, lisa).

parent(mike, david).
parent(anna, david).

father(F, C) :-
    male(F),
    parent(F, C).

mother(M, C) :-
    female(M),
    parent(M, C).

grandfather(GF, C) :-
    male(GF),
    parent(GF, P),
    parent(P, C).

grandmother(GM, C) :-
    female(GM),
    parent(GM, P),
    parent(P, C).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
