def dfs(graph, node, seen, destination):
    if node not in seen:
        seen.append(node)
        if node == destination:
            return seen
        for neighbour in graph[node]:
            if neighbour not in seen:
                dfs(graph, neighbour, seen, destination)
    return seen
graph = {
    'M': ['R', 'Q', 'N'],
    'N': ['M', 'Q', 'O'],
    'O': ['N', 'P'],
    'R': ['M'],
    'Q': ['M', 'N', 'P'],
    'P': ['O', 'Q']
}
print(dfs(graph, 'M', [], 'P'))
