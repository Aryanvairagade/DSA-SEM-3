
from collections import deque

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    visited = [False] * n
    queue = deque()

    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

start = int(input("Enter starting vertex: "))

print("BFS Traversal:")
bfs(start)
