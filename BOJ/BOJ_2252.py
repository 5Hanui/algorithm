from collections import deque
N, M = map(int, input().split())
indegree = [0 for i in range(N+1)]
graph = [[] for i in range(N+1)]
result = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    global result
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topology_sort()

for i in range(len(result)):
    print(result[i], end = ' ')