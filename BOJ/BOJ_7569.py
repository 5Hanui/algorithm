from collections import deque
M, N, H = map(int, input().split())
box = []
tomato = []
no = 0
to = 0
tox = 0
dir = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

visit = []
for i in range(H):
    a = []
    for j in range(N):
        b = []
        for k in range(M):
            b.append(0)
        a.append(b)
    visit.append(a)
q = deque()
days = 0
for i in range(H):
    arr = []
    for j in range(N):
        a = input().split()
        for k in range(len(a)):
            if a[k] == '1':
                q.append((i, j, k))
                visit[i][j][k] = 1
                to += 1
            if a[k] == '0': tox += 1
            if a[k] == '-1': no += 1
        arr.append(a)
    box.append(arr)

def bfs():
    global tox, to, days
    while q:
        cur = q.popleft()
        zc, zy, zx = cur[0], cur[1], cur[2]

        for i in range(6):
            next_cur = (zc + dir[i][0], zy + dir[i][1], zx + dir[i][2])
            if next_cur[0] < 0 or next_cur[0] >= H or next_cur[1] < 0 or next_cur[1] >= N or next_cur[2] < 0 or next_cur[2] >= M:
                continue
            if box[next_cur[0]][next_cur[1]][next_cur[2]] == '-1' or box[next_cur[0]][next_cur[1]][next_cur[2]] == '1':
                continue
            if box[next_cur[0]][next_cur[1]][next_cur[2]] == '0' and visit[next_cur[0]][next_cur[1]][next_cur[2]] == 0:
                tox -= 1
                to += 1
                box[next_cur[0]][next_cur[1]][next_cur[2]] = '1'
                visit[next_cur[0]][next_cur[1]][next_cur[2]] = visit[zc][zy][zx] + 1
                q.append((next_cur[0], next_cur[1], next_cur[2]))
                days = max(days, visit[next_cur[0]][next_cur[1]][next_cur[2]])


if to + no == N * M * H:
    print("0")
    exit(0)
else:
    bfs()
    if tox > 0:
        print("-1")
    else:
        print(days-1)





