from collections import deque
import heapq
N, M, P = map(int, input().split())
d = [[0 for i in range(N+1)] for _ in range(N+1)]
cus = [False for i in range(M)]
start = []
end = []
xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(N):
    arr = list(map(int, input().split()))
    d[i+1][1:N+1] = arr
taxi_y, taxi_x = map(int, input().split())
for j in range(M):
    sy, sx, ey, ex = map(int, input().split())
    start.append((sy, sx))
    end.append((ey, ex))

# 출발지와 도착지 거리 계산
def bfs():
    global taxi_y, taxi_x, P
    visit = [[-1 for i in range(N+1)] for _ in range(N+1)]
    q = deque()
    visit[taxi_y][taxi_x] = 0
    q.append((taxi_y, taxi_x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + xy[i][0], x + xy[i][1]
            if 1<=ny<=N and 1<=nx<=N:
                if d[ny][nx] == 0 and visit[ny][nx] == -1:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny, nx))
    return visit


def findCustomer():
    global P
    visit = bfs()
    h = []
    for i in range(M):
        if cus[i] is False:
            y, x = start[i][0], start[i][1]
            dist = visit[y][x]
            if P - dist >= 0 and dist != -1:
                heapq.heappush(h, (dist, y, x, i))
    if not h:
        return -1
    dist, ny, nx, idx = heapq.heappop(h)
    P -= dist
    cus[idx] = True
    return idx


def move(g_idx):
    global P
    visit = bfs()
    y, x = end[g_idx][0], end[g_idx][1]
    dist = visit[y][x]
    if P - dist < 0:
        return -1
    return dist


ok = True
cnt = M
while cnt:
    guest = findCustomer()
    if guest == -1:
        ok = False
        break
    taxi_y, taxi_x = start[guest][0], start[guest][1]
    p = move(guest)
    if p == -1:
        ok = False
        break
    P += p
    taxi_y, taxi_x = end[guest][0], end[guest][1]
    cnt -= 1

if ok:
    print(P)
else:
    print(-1)