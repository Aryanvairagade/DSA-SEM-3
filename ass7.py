
n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * n

def dfs(v):
    print(v, end=" ")
    visited[v] = True

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start)
