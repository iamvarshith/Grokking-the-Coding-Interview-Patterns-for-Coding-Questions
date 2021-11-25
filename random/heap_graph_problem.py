# Using a Python dictionary to act as an adjacency list and find the kth largest Number in a given graph
import heapq

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
    return visited


def kth_max_element(k, visited, graph, node):
    heap = dfs(visited, graph, node)
    heap = list(heap)
    heapq.heapify(heap)
    kth = heapq.nlargest(k, heap)
    print(f"largest {kth[k-1]}")


# Driver Code
if __name__ == '__main__':
    kth_max_element(2, visited, graph, 25)
