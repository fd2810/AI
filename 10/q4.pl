dog(t).
dog(b).
dog(l).
dog(r).
animal(X):-dog(X).
pet(X):-animal(X).
living(X):-pet(X).
