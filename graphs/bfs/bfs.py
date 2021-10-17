# Using a Python dictionary to act as an adjacency list


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


class Graph:
    def __init__(self, edges, nodes):
        self.adj = {}
        for i in nodes:
            self.adj[i] = []
        for j in edges:
            if j.src in self.adj:
                self.adj[j.src].append(j.dest)


def printGraph(graph):
    for node in graph.adj:
        print(f"{node} -> {graph.adj[node]}")


visited = []
queue = []


def bfs(graph, node):
    queue.append(node)
    visited.append(node)
    while queue:
        current_element = queue.pop(0)
        print(current_element, end=" ")

        for element in graph[current_element]:
            if element not in visited:
                visited.append(element)
                queue.append(element)


if __name__ == '__main__':
    # Input: Edges in a directed graph
    edges = [Edge('A', "B"), Edge("A", "C"), Edge("B", "E"), Edge("B", "D"),
             Edge("E", "F"), Edge("C", "F")]

    vertices = ["A", "B", "C", "D", "E", "F"]
    # construct a graph from a given list of edges
    graph = Graph(edges=edges, nodes=vertices)
    print(graph.adj)
    bfs(graph.adj, "A")

    # print adjacency list representation of the graph
