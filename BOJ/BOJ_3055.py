from collections import deque
# .: 빈곳, *:물, X:돌, D: 비버의 굴, S:고슴도치
R, C = map(int, input().split())
waters = [[0 for i in range(C)] for _ in range(R)]
doc = [[0 for i in range(C)] for _ in range(R)]
d = []
xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
wq = deque()
dq = deque()
sy, sx = 0, 0
for i in range(R):
    string = input()
    for j in range(len(string)):
        if string[j] == '*':
            wq.append((i, j))
            waters[i][j] = 1
        elif string[j] == 'S':
            dq.append((i, j))
            doc[i][j] = 1
        elif string[j] == 'D':
            sy, sx = i, j
    d.append(list(string))
def bfs_water():
    while wq:
        cur_w = wq.popleft()
        for i in range(4):
            next_w = (cur_w[0] + xy[i][0], cur_w[1] + xy[i][1])
            if next_w[0] < 0 or next_w[0] >= R or next_w[1] < 0 or next_w[1] >= C:
                continue
            if d[next_w[0]][next_w[1]] == 'D' or d[next_w[0]][next_w[1]] == 'X' or waters[next_w[0]][next_w[1]] > 0:
                continue
            waters[next_w[0]][next_w[1]] = waters[cur_w[0]][cur_w[1]] + 1
            wq.append((next_w[0], next_w[1]))

def bfs_dochi():
    while dq:
        cur = dq.popleft()
        for i in range(4):
            next_cur = (cur[0] + xy[i][0], cur[1] + xy[i][1])
            if next_cur[0] < 0 or next_cur[0] >= R or next_cur[1] < 0 or next_cur[1] >= C:
                continue
            if d[next_cur[0]][next_cur[1]] == 'X' or doc[next_cur[0]][next_cur[1]] > 0: continue
            if next_cur[0] == sy and next_cur[1] == sx:
                doc[next_cur[0]][next_cur[1]] = doc[cur[0]][cur[1]] + 1
                return
            if doc[cur[0]][cur[1]] + 1 < waters[next_cur[0]][next_cur[1]] or waters[next_cur[0]][next_cur[1]] == 0:
                doc[next_cur[0]][next_cur[1]] = doc[cur[0]][cur[1]] + 1
                dq.append((next_cur[0], next_cur[1]))

# 물 이동
bfs_water()
# 고슴도치 이동
bfs_dochi()
if doc[sy][sx] != 0:
    print(doc[sy][sx] - 1)
else:
    print("KAKTUS")

