adj=[[2, 3, 1], [0], [0, 4], [0], [2]]

graph={}
for i in range(len(adj)):
    graph[i] = adj[i]

visited=[]
queue=[]
def bfs(visited,node,graph):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m , end=" ")
        
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

bfs(visited,0,graph )


