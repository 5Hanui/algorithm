import heapq, sys
N = int(input())
d = [0 for i in range(N+1)]
edge = [[]for i in range(N+1)]
degree = [0 for i in range(N+1)]
time = [0 for i in range(N+1)]
h = []
for i in range(1, N+1):
    n = list(map(int, input().split()))
    for j in range(len(n)):
        if n[j] == -1:
            break
        if j == 0:
            d[i] = n[j]
        else:
            degree[i] += 1
            edge[n[j]].append(i)

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(h, i)
while h:
    now = heapq.heappop(h)
    if time[now] == 0:
        time[now] = d[now]
    for e in edge[now]:
        degree[e] -= 1
        if degree[e] == 0:
            heapq.heappush(h, e)
        time[e] = max(time[now] + d[e], time[e])
for i in range(1, N+1):
    print(time[i])

