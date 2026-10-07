from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True

def get_next_states(state):
    m_left, c_left, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    next_states = []

    for m, c in moves:
        if boat == 1:  
            new_state = (m_left - m, c_left - c, 0)
        else:          
            new_state = (m_left + m, c_left + c, 1)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for next_state in get_next_states(state):
                new_path = list(path)
                new_path.append(next_state)
                queue.append(new_path)

    return None

solution = bfs()

if solution:
    print("Missionaries and Cannibals Solution:\n")
    step = 0
    for state in solution:
        m_left, c_left, boat = state
        side = "Left" if boat == 1 else "Right"
        print(f"Step {step}:")
        print(f" Left Bank : {m_left} Missionaries, {c_left} Cannibals")
        print(f" Right Bank: {3-m_left} Missionaries, {3-c_left} Cannibals")
        print(f" Boat is on {side} Bank\n")
        step += 1
else:
    print("No solution found.")
