N, M = map(int, input().split())
m = []
cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
wind = []
xy = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for i in range(N):
    arr = list(map(int, input().split()))
    m.append(arr)
for i in range(M):
    di, si = map(int, input().split())
    wind.append((di, si))

def moveCloud(d, s):
    global wind, cloud, N, m
    tmp = []
    for i in range(len(cloud)):
        y, x = cloud[i]
        ny, nx = y, x
        for j in range(s):
            ny, nx = ny + xy[d][0], nx + xy[d][1]
            if ny >=N:
                ny = 0
            elif ny < 0:
                ny = N-1
            if nx >= N:
                nx = 0
            elif nx < 0:
                nx = N-1
        tmp.append((ny, nx))
    cloud = tmp

    addRain()


def addRain():
    global cloud, N, m
    for i in range(len(cloud)):
        y, x = cloud[i]
        m[y][x] += 1
    tmp = cloud
    cloud = []

    copyRain(tmp)

def copyRain(l):
    global cloud, N, m
    xDir = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    for i in range(len(l)):
        y, x = l[i]
        cnt = 0
        for j in range(4):
            ny, nx = y + xDir[j][0], x + xDir[j][1]
            if 0 <= ny < N and 0 <= nx < N:
                if m[ny][nx] > 0:
                    cnt += 1
        m[y][x] += cnt

    makeCloud(l)

def makeCloud(l):
    global cloud, m
    for i in range(N):
        for j in range(N):
            if (i, j) not in l:
                if m[i][j] >= 2:
                    cloud.append((i, j))
                    m[i][j] -= 2


answer = 0
for i in range(M):
    moveCloud(wind[i][0], wind[i][1])
for y in range(N):
    for x in range(N):
        answer += m[y][x]
print(answer)
