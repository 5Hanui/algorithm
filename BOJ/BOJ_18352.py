import sys, heapq
inf = sys.maxsize

N, M, K, X = map(int, input().split())
ans = 0
d = [[] for _ in range(N+1)]
dp = [inf for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)

heap = []
def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        w, cur = heapq.heappop(heap)
        if dp[cur] < w: continue
        for node in d[cur]:
            if dp[node] > dp[cur] + 1:
                dp[node] = dp[cur] + 1
                heapq.heappush(heap, (dp[node], node))

Dijkstra(X)
ans = 0
for i in range(1, N+1):
    if dp[i] == K:
        ans += 1
        print(i)

if ans == 0:
    print(-1)