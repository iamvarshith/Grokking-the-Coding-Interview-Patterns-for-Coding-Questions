# Using a Python dictionary to act as an adjacency list
graph = {
    25: [5, 87],
    5: [45, 63],
    45: [93],
    11: [],
    53: [69],
    47: []
}

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            try:
                dfs(visited, graph, neighbour)
            except:
                pass


# Driver Code
if __name__ == '__main__':
    dfs(visited, graph, 25)
