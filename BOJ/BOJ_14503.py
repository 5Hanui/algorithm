N, M = map(int, input().split())
robot = list(map(int, input().split()))
m = list()
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]
direct = {0: 3, 1: 0, 2: 1, 3: 2}
visit = [[1]*M for _ in range(N)]
ans = 0
for j in range(N):
    row = list(map(int, input().split()))
    m.append(row)


def solution(r, c, d):
    global ans
    while True:
        cnt = 0
        # 1. 현재 위치를 청소한다.
        if visit[r][c] == 1 and m[r][c] == 0:
            ans += visit[r][c]
            visit[r][c] = 0
        temp_d = d
        for i in range(4):
            next_y, next_x = r + dir[temp_d][0], c + dir[temp_d][1]
            if 0 > next_y or next_y >= N or 0 > next_x or next_x >= M or visit[next_y][next_x] == 0 or m[next_y][next_x] == 1:
                cnt += 1
                temp_d = direct.get(temp_d)
                continue
            else:
                if visit[next_y][next_x] == 1 and m[next_y][next_x] == 0:
                    r, c, d = next_y, next_x, direct.get(temp_d)
                    break
                else:
                    d = temp_d
                    temp_d = direct.get(temp_d)
                    continue
        if cnt == 4:
            back_y, back_x = r + back[d][0], c + back[d][1]
            if 0 > back_y or back_y >= N or 0 > back_x or back_x >= M or m[back_y][back_x] == 1:
                return
            else:
                r, c = back_y, back_x
                continue

solution(robot[0], robot[1], robot[2])
print(ans)