# Using a Python dictionary to act as an adjacency list
graph = {
    1: [4, 3, 2],
    2: [],
    3: [4],
    4: [],
    5: [6],
    6: [],
    7: [8, 9],
    8: [],
    9: []

}

visited = set()  # Set to keep track of visited nodes.


def connected_graph(visited, graph):
    connected_found = 0
    temp_comp = []
    for i in graph:

        if i not in visited:
            connected_found += 1
            temp_comp.append([])
            dfs(visited, graph, i, temp_comp, connected_found - 1)
    return connected_found, temp_comp


def dfs(visited, graph, node, temp_comp, connected_found):
    if node not in visited:
        print(node)

        visited.add(node)
        temp_comp[connected_found].append(node)

        for neighbour in graph[node]:
            # print(neighbour)
            dfs(visited, graph, neighbour, temp_comp, connected_found)


# Driver Code
print('answer ' + str(connected_graph(visited, graph)))
