xy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
d = []
def bfs(r, c):
    global d
    count = [[0 for i in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if d[i][j] == '*':
                count[i][j] = '*'
                continue
            for k in range(8):
                ny, nx = i + xy[k][0], j + xy[k][1]
                if ny < 0 or ny >= r or nx < 0 or nx >= c: continue
                if d[ny][nx] == '*':
                    count[i][j] += 1
    for i in range(r):
        for j in range(c):
            print(count[i][j], end = '')
        print()


while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0: break
    d = []
    for i in range(R):
        string = list(input())
        d.append(string)
    bfs(R, C)

