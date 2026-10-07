def associative_addition(a, b, c):
    left = (a + b) + c
    right = a + (b + c)
    print(f"\nAddition Law:")
    print(f"(a + b) + c = ({a} + {b}) + {c} = {left}")
    print(f"a + (b + c) = {a} + ({b} + {c}) = {right}")
    if (left==right):
        print("They equal ")
    else :
        print("They are not equal")
def associative_multiplication(a, b, c):
    left = (a * b) * c
    right = a * (b * c)
    print(f"\nMultiplication Law:")
    print(f"(a * b) * c = ({a} * {b}) * {c} = {left}")
    print(f"a * (b * c) = {a} * ({b} * {c}) = {right}")
    if (left==right):
        print("They equal ")
    else :
        print("They are not equal")
def associative_and(a, b, c):
    left = (a and b) and c
    right = a and (b and c)
    print(f"\nAssociative Law for AND:")
    print(f"(a and b) and c = ({a} and {b}) and {c} = {left}")
    print(f"a and (b and c) = {a} and ({b} and {c}) = {right}")
    if left == right:
        print("They are equal")
    else:
        print("They are not equal")

def associative_or(a, b, c):
    left = (a or b) or c
    right = a or (b or c)
    print(f"\nAssociative Law for OR:")
    print(f"(a or b) or c = ({a} or {b}) or {c} = {left}")
    print(f"a or (b or c) = {a} or ({b} or {c}) = {right}")
    if left == right:
        print("They are equal")
    else:
        print("They are not equal")
# --- MAIN PROGRAM ---
if __name__ == "__main__":
    print("Associative Law Demonstration\n")
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))

    associative_addition(a, b, c)
    associative_multiplication(a, b, c)
    associative_and(a, b, c)
    associative_or(a, b, c)


'''# --- MAIN PROGRAM ---
if __name__ == "__main__":
    print("Associative Law Demonstration\n")
    a = bool(int(input("Enter value for a (0 or 1): ")))
    b = bool(int(input("Enter value for b (0 or 1): ")))
    c = bool(int(input("Enter value for c (0 or 1): ")))

    associative_addition(int(a), int(b), int(c))
    associative_multiplication(int(a), int(b), int(c))
'''
