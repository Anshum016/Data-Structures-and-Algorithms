adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

graph = {}
for i in range(len(adj)):
    graph[i] = adj[i]

visited = []
stack = []

def dfs(visited, node, graph):
    stack.append(node)

    while stack:
        m = stack.pop()
        if m not in visited:
            visited.append(m)
            print(m, end=" ")

            for i in reversed(graph[m]):
                if i not in visited:
                    stack.append(i)

dfs(visited, 0, graph)
