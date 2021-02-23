import sys
input = sys.stdin.readline
R, C = map(int, input().split())
yx = [(-1, 1), (0, 1), (1, 1)]
d = []
visit = [[False for i in range(C)]for _ in range(R)]
ans = 0
for i in range(R):
    arr = list(input())
    d.append(arr)

def dfs(y, x):
    global ans
    if x == C-1:
        ans += 1
        return True
    for i in range(3):
        ny, nx = y + yx[i][0], x + yx[i][1]
        if ny < 0 or nx < 0 or ny >= R or nx >= C: continue

        if d[ny][nx] != 'x' and visit[ny][nx] is False:
            visit[ny][nx] = True
            isFind = dfs(ny, nx)
            if isFind: return True

    return False

for r in range(R):
    if d[r][0] != 'x':
        dfs(r, 0)
print(ans)