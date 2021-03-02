# N <= 200000이고 제한시간이 1초이므로, O(logN)인 우선순위 큐 사용

import heapq
h = []
tq = []
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    h.append((a, b))
h.sort()
heapq.heappush(tq, h[0][1])
for i in range(1, N):
    # 가장 빨리 끝나는 t를 찾아낸다.
    t = heapq.heappop(tq)
    if t <= h[i][0]:
        heapq.heappush(tq, h[i][1])
    else: # 겹치면 다시 큐에 넣는다.
        heapq.heappush(tq, t)
        heapq.heappush(tq, h[i][1])

print(len(tq))