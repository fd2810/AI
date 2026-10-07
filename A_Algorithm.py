graph = {
    "A": ({"B": 1, "D": 2, "E": 3}, 4),
    "B": ({"D": 1, "C": 2}, 3),
    "C": ({"F": 3}, 2),
    "D": ({"F": 2}, 3),
    "E": ({"D": 3, "F": 4}, 2),
    "F": ({}, 0)
}

def get_min(q):
    mn = None

    for i in q:
        if mn is None or sum(q[i]) < sum(q[mn]):
            mn = i
    return mn
def a_star(graph, prev, dst, path, path_cost, q):
    print("A* value for", prev, "is", path_cost)
    for n in graph[prev][0]:
        if n not in path:
            q[n] = (
                path_cost + graph[prev][0][n],
                graph[n][1]
            )
    while q:
        mn = get_min(q)
        print("Selecting minimum vertex", mn)
        if dst == mn:
            return path + [dst]
        pc = q[mn][0]
        print("Previous path cost:", pc)
        q.pop(mn)
        new_path = a_star(
            graph,
            mn,
            dst,
            path + [mn],
            pc,
            q
        )
        if new_path:
            return new_path
    return []
source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")
path = a_star(
    graph,
    source,
    dest,
    [source],
    0,
    {source: (0, graph[source][1])}
)
print("Final Path:", path)
