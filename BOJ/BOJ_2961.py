import sys
ans = sys.maxsize
S = []
B = []
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    S.append(x)
    B.append(y)

visit = [False for i in range(N)]
s, b = 1, 0
def backtrack(idx):
    global s, b, ans
    if idx > N:
        return
    ans = min(ans, abs(s-b))
    for j in range(idx, N):
        if visit[j] is False:
            s *= S[j]
            b += B[j]
            visit[j] = True
            backtrack(j)
            visit[j] = False
            s = s // S[j]
            b -= B[j]


for i in range(N):
    if visit[i] is False:
        visit[i] = True
        s, b = S[i], B[i]
        backtrack(i)
        visit[i] = False
        s, b = 1, 0

print(ans)