book(p).
book(h).
book(m).
book(c).
ks(X):-book(X).
em(X):-ks(X).
vr(X):-em(X).
