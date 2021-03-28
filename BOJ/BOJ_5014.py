import sys
from collections import deque
F, S, G, U, D = map(int, input().split())
ans = [sys.maxsize for i in range(F+1)]
visit = [False for i in range(F+1)]
q = deque()
q.append(S)
visit[S] = True
ans[S] = 0
while q:
    cur = q.popleft()
    if cur == G:
        continue
    for i in [U, -D]:
        next_p = cur + i
        if 1 <= next_p <= F and visit[next_p] is False:
            q.append(next_p)
            visit[next_p] = True
            ans[next_p] = min(ans[cur] + 1, ans[next_p])
if visit[G] is False:
    print("use the stairs")
else:
    print(ans[G])