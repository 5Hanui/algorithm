from collections import deque
import copy
N, M = map(int, input().split())
d = []
wall = []
virus = []
xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(N):
    arr = list(map(int, input().split()))
    d.append(arr)
    for j in range(len(arr)):
        if arr[j] == 0:
            wall.append((i, j))
        if arr[j] == 2:
            virus.append((i, j))
visit = [False for i in range(len(wall))]
original = copy.deepcopy(d)
answer = 0
def moveVirus():
    global d, virus
    tmp = copy.deepcopy(d)
    s = 0
    q = deque(virus)
    while q:
        cur = q.popleft()
        y, x = cur[0], cur[1]
        for k in range(4):
            ny, nx = y + xy[k][0], x + xy[k][1]
            if 0 <= ny < N and 0 <= nx < M:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = 2
                    q.append((ny, nx))
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                s += 1
    return s


def backtracking(cnt, idx):
    global answer, wall, d, original
    if cnt == 3:
        ans = moveVirus()
        answer = max(ans, answer)
        return

    for i in range(idx, len(wall)):
        if visit[i] is False:
            visit[i] = True
            d[wall[i][0]][wall[i][1]] = 1
            backtracking(cnt+1, idx+1)
            d[wall[i][0]][wall[i][1]] = 0
            visit[i] = False

backtracking(0, 0)
print(answer)



