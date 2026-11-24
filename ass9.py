
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    parent[xroot] = yroot

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input(
        "Enter source destination weight: ").split())

    edges.append((w, u, v))

edges.sort()

parent = [i for i in range(n)]

cost = 0

print("Minimum Spanning Tree:")

for w, u, v in edges:
    x = find(parent, u)
    y = find(parent, v)

    if x != y:
        print(u, "-", v, ":", w)
        union(parent, x, y)
        cost += w

print("Minimum Cost:", cost)
