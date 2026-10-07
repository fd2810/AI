import heapq
graph = {
    'a': [['b', 1], ['d', 2], ['e', 3], 4],
    'b': [['a', 1], ['c', 2], ['d', 3], 3],
    'c': [['f', 2], 2],
    'd': [['f', 2], 3],
    'e': [['d', 3], ['f', 2], 2],
    'f': [0]
}
def greedy_search(graph, source, goal):
    queue = [(graph[source][-1], source, [source])]
    visited = set()
    while queue:
        h, current, path = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path
        print("Current node:", current)
        neighbours = graph[current][:-1]
        for neighbour in neighbours:
            node = neighbour[0]
            cost = neighbour[1]
            if node not in visited:
                heuristic = graph[node][-1]
                print(node, "->", heuristic)
                heapq.heappush(
                    queue,
                    (heuristic, node, path + [node])
                )
    return None
source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")
path = greedy_search(graph, source, dest)
if path:
    print("Path:", path)
else:
    print("Path not found")
