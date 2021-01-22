from collections import deque
N = int(input())
d = list(range(10))
result = []
q = deque(d)
while q:
    cur = q.pop()
    result.append(cur)
    if cur % 10 == 0: continue
    for j in range(0, cur % 10):
        if cur > j:
            q.append(cur*10+j)
result.sort()
if N >= 1023:
    print(-1)
else:
    print(result[N])