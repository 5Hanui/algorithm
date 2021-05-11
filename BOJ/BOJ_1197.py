V, E = map(int, input().split())
graph = []
mst_cost = 0
for i in range(E):
    u, v, w = map(int, input().split())
    # 가중치, 간선 순서로 넣는다.
    graph.append((w, u, v))
parent = list(range(V+1))
graph.sort() # 가중치가 작은 순서로 정렬


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 == root2:
        return
    parent[root2] = root1

for e in graph:
    w, a, b = e
    if find(a) != find(b):
        union(a, b)
        mst_cost += w
print(mst_cost)

