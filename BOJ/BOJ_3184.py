from collections import deque
R, C = map(int, input().split())
d = []
visit = [[False for c in range(C)] for r in range(R)]
xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(R):
    c = list(input())
    d.append(c)
def bfs(y, x):
    q = deque()
    q.append((y, x))
    visit[y][x] = True
    sheep = 0
    wolf = 0
    if d[y][x] == 'o':
        sheep += 1
    if d[y][x] == 'v':
        wolf += 1
    while len(q) != 0:
        cur = q.popleft()
        for p in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y = cur[0] + p[0]
            next_x = cur[1] + p[1]
            if next_x < 0 or next_y < 0 or next_x >= C or next_y >= R or visit[next_y][next_x] or d[next_y][next_x] == '#':
                continue
            if d[next_y][next_x] != '#' and not visit[next_y][next_x]:
                if d[next_y][next_x] == 'o':
                    sheep += 1
                if d[next_y][next_x] == 'v':
                    wolf += 1
                q.append((next_y, next_x))
                visit[next_y][next_x] = True
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf


s = 0
w = 0
for i in range(R):
    for j in range(C):
        if d[i][j] != '#' and not visit[i][j]:
            sh, wf = bfs(i, j)
            s += sh
            w += wf
print(s, w)