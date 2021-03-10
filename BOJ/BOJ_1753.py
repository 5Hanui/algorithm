import sys, heapq
V, E = map(int, input().split())
start = int(input())
m = [[] for _ in range(V+1)]
d = [sys.maxsize for i in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    m[u].append((v, w))
d[start] = 0
h = []
heapq.heappush(h, (0, start))
while h:
    w, cur = heapq.heappop(h)
    if d[cur] < w: continue
    for next_cur, weight in m[cur]:
        dis = w + weight
        if dis < d[next_cur]:
            d[next_cur] = dis
            heapq.heappush(h, (dis, next_cur))

for i in range(1, V+1):
    if d[i] != sys.maxsize:
        print(d[i])
    else:
        print("INF")



