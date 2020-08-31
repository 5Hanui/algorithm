from collections import deque

global d, visit, w, h
xy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def bfs(y, x):
    queue = deque()
    queue.append((x, y))
    visit[y][x] = True
    while len(queue) != 0:
        cur = queue.popleft()
        for idx in range(8):
            next_p = (cur[0] + xy[idx][0], cur[1] + xy[idx][1])
            if next_p[0] < 0 or next_p[1] < 0 or next_p[0] >= w or next_p[1] >= h:
                continue;
            if d[next_p[1]][next_p[0]] == 1 and visit[next_p[1]][next_p[0]] is False:
                visit[next_p[1]][next_p[0]] = True
                queue.append(next_p)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    d = []
    num = 0
    for i in range(h):
        row = list(map(int, input().split()))
        d.append(row)
    visit = [[False for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if d[i][j] == 1 and visit[i][j] is False:
                bfs(i, j)  # y,x
                num += 1
    print(num)

# def bfs(x, y):
