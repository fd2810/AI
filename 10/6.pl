male(Alex).
male(Edward).
male(Charlie).
female(Beth).
female(Fiona).
female(Diana).
parent(Alex,Charlie).
parent(Alex,Diana).
parent(Beth,Charlie).
parent(Beth,Diana).
parent(Diana,Fiona).
parent(Edward,Fiona).

father(F,C):-male(F),parent(F,C).
mother(M,C):-female(M),parent(M,C).

grandfather(GF,C):-male(GF),parent(GF,P),parent(P,C).
grandmother(GM,C):-female(GM),parent(GM,P),parent(P,C).

sibling(X,Y):-parent(P,X),parent(P,Y),X\=Y.
