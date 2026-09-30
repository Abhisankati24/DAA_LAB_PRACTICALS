n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = set()

def dfs(vertex):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour)

print("DFS Traversal:", end=" ")
dfs(start)