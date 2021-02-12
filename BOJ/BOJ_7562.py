from collections import deque
T = int(input())
d = []
dir = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]


def bfs(y, x, yy, xx):
    q = deque()
    q.append((y, x))
    while q:
        cur = q.popleft()
        cur_y, cur_x = cur[0], cur[1]
        for i in range(8):
            next_y, next_x = cur_y + dir[i][0], cur_x + dir[i][1]
            if next_y < 0 or next_x < 0 or next_x >= n or next_y >= n:
                continue
            if visit[next_y][next_x] > 0:
                continue
            visit[next_y][next_x] = visit[cur_y][cur_x] + 1
            q.append((next_y, next_x))
            if next_y == yy and next_x == xx:
                return


for i in range(T):
    visit = []
    n = int(input())
    for i in range(n):
        temp = []
        v = []
        for j in range(n):
            temp.append(0)
            v.append(0)
        d.append(temp)
        visit.append(v)
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    if sy == ey and sx == ex:
        print("0")
    else:
        bfs(sy, sx, ey, ex)
        print(visit[ey][ex])


