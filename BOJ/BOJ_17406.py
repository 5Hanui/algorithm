import copy
N, M, K = map(int, input().split())
d = []
for i in range(N):
    arr = list(map(int, input().split()))
    d.append(arr)
ori = copy.deepcopy(d)
check = [False for i in range(K)]
order = []
cmd = []
answer = float('inf')

def spiral(r, c, s):
    global d
    tmp = copy.deepcopy(d)
    k = s
    sy, sx = r-s, c-s
    ey, ex = r+s, c+s
    # 윗칸
    for i in range(k):
        ny = sy+i
        for x in range(sx+i, ex-i):
            tmp[ny][x+1] = d[ny][x]
    # 오른쪽
    for i in range(k):
        nx = ex-i
        for y in range(sy+i, ey-i):
            tmp[y+1][nx] = d[y][nx]
    # 아래
    for i in range(k):
        ny = ey-i
        for x in range(ex-i, sx+i, -1):
            tmp[ny][x-1] = d[ny][x]

    # 윗칸
    for i in range(k):
        nx = sx+i
        for y in range(ey-i, sy+i, -1):
            tmp[y-1][nx] = d[y][nx]
    d = tmp


for i in range(K):
    R, C, S = map(int, input().split())
    cmd.append((R-1, C-1, S))


def backtracking(cnt):
    global K, d, ori, answer
    if cnt == K:
        d = ori
        ans = float('inf')
        for i in range(K):
            r, c, s = cmd[order[i]]
            spiral(r, c, s)
        for i in range(len(d)):
            ans = min(ans, sum(d[i]))
        answer = min(answer, ans)
        return

    for i in range(K):
        if check[i] is False:
            check[i] = True
            order.append(i)
            backtracking(cnt+1)
            check[i] = False
            order.pop()


for i in range(K):
    if check[i] is False:
        check[i] = True
        order.append(i)
        backtracking(1)
        check[i] = False
        order.pop()

print(answer)
