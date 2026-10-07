from collections import deque

#Function to check if this state is already visited]
def is_visited(state, visited):
    return state in visited

#BFS algorithm to solve the water jug problem
def water_jug_bfs():
    max_a, max_b, = 3, 2 #Capacities of the jugs
    visited = set() #To keep track of visited states
    queue = deque() #For BFS

    #Start from empty jugs
    queue.append((0, 0)) #(amount_in_jugA, amount_in_jugB)

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(f"Jug A: {a}L, Jug B: {b}L")

        if a == 1 or b == 1:
            print("Found a solution!")
            return

        #All
        possible_states = [
                (max_a, b),
                (a, max_b),
                (0, b),
                (a, 0),
                (min(a + b, max_a), b - (min(a + b, max_a) - a)),
                (a - (min(a + b, max_b) - b), min(a + b, max_b))
            ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)

        print("No solution found.")

#Run the function
water_jug_bfs()
