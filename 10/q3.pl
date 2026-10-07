student(a).
student(b).
student(c).
student(d).
learner(X):-student(X).
knowledge(X):-learner(X).
future(X):-knowledge(X).

