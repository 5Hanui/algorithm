from collections import deque
import copy
N, K = map(int, input().split())
string = str(N)
arr = list(str(N))
ans = -1
q = deque()
d = dict()
for i in range(1, K+1):
    d[i] = []
def bfs(k):
    global ans, arr
    while q:
        cur, cur_cnt = q.popleft()
        if cur_cnt == k:
            ans = max(ans, int(cur))
            continue
        l = list(cur)
        for i in range(0, len(arr)-1):
            for j in range(i + 1, len(arr)):
                c = copy.deepcopy(l)
                if i == 0 and c[j] == '0':
                    continue
                c[i], c[j] = c[j], c[i]
                if ''.join(c) in d[cur_cnt+1]:
                    continue
                d[cur_cnt + 1].append(''.join(c))
                q.append((''.join(c), cur_cnt + 1))


q.append((str(N), 0))
bfs(K)
print(ans)