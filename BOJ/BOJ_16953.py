from collections import deque
A, B = map(int, input().split())
q = deque()
q.append((1, B))
isOk = False
while q:
    step, cur = q.popleft()
    if cur == A:
        print(step)
        exit(0)
    isOk = False
    if cur % 2 == 0:
        isOk = True
        q.append((step+1, cur // 2))
    if cur >= 10 and cur % 10 == 1:
        isOk = True
        q.append((step+1, (cur - 1) // 10))
    if isOk is False:
        break
print(-1)