from collections import deque
N, K = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(str(i))
temp = 0
ans = []
while q:
    cur = q.popleft()
    temp += 1
    if temp != K:
        q.append(cur)
    else:
        ans.append(cur)
        temp = 0
if len(ans) == 1:
    print("<"+ans[0]+">")
    exit(0)
for i in range(0, len(ans)):
    if i == 0:
        print("<" + ans[0], end=', ')
    elif i == len(ans)-1:
        print(ans[-1], end='>')
    else:
        print(ans[i], end=', ')
