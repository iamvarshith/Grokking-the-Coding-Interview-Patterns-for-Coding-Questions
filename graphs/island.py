matrix = [[1, 1, 0, 0, 0],
          [0, 1, 0, 0, 1],
          [1, 0, 0, 1, 1],
          [0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1]
          ]


def island_finder(graph: list):
    no_of_islands = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                print(str(graph) + ' ' + str(no_of_islands))
                no_of_islands += 1

                dfs(i, j, graph)
    print(no_of_islands)


def dfs(i, j, graph):
    n = len(graph[0])
    m = len(graph)
    if i < 0 or i >= m or j < 0 or j >= n or graph[i][j] != 1:
        return
    graph[i][j] = 2

    dfs(i, j + 1, graph)
    dfs(i, j - 1, graph)
    dfs(i + 1, j, graph)
    dfs(i - 1, j, graph)


island_finder(matrix)
