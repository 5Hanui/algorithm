N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
edges = []
ans = 0
for i in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if u == v:
        return
    parent[y] = x


for edge in edges:
    weight, s, e = edge
    if find(s) != find(e):
        union(s, e)
        ans += weight
print(ans)


