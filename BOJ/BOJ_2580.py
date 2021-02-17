import sys
input = sys.stdin.readline

maps = []
todo = 0
to = []
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] == 0:
            todo += 1
            to.append((i, j))
    maps.append(arr)
def findNum(y, x, n):
    # 가로줄
    for i in maps[y]:
        if i == n:
            return False
    # 세로줄
    for j in range(9):
        if maps[j][x] == n:
            return False

    # 사각형
    yy, xx = (y // 3) * 3, (x // 3) * 3
    for _y in range(yy, yy + 3):
        for _x in range(xx, xx + 3):
            if maps[_y][_x] == n:
                return False
    return True

def backtrack(ix):
    global todo
    if ix == todo:
        for _ in range(9):
            for __ in range(9):
                print(maps[_][__], end=' ')
            print()
        exit(0)

    ny, nx = to[ix][0], to[ix][1]
    for _k in range(1, 10):
        if maps[ny][nx] == 0 and findNum(ny, nx, _k):
            maps[ny][nx] = _k
            backtrack(ix+1)
            maps[ny][nx] = 0


backtrack(0)