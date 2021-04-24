R, C, M = map(int, input().split())
table = [[0 for i in range(C)] for _ in range(R)]
xy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
shark = {}
answer = 0
for i in range(M):
    # y, x, s: 속력, d: 이동방향, z:크기
    r, c, s, d, z = map(int, input().split())
    table[r-1][c-1] = i + 1
    shark[i+1] = [s, d, z]

p_idx = -1

def fishing():
    global p_idx, R, C, table, answer, shark
    # print(p_idx)
    for i in range(R):
        if table[i][p_idx] > 0:
            shark_idx = table[i][p_idx]
            answer += shark[shark_idx][2]
            table[i][p_idx] = 0
            # print(shark[shark_idx][2], " 잡음")
            break

def moveShark():
    global p_idx, R, C, table, answer, shark, xy
    tmp = [[0 for i in range(C)] for _ in range(R)]
    # 주어진 속도로 이동,
    # 경계를 넘으면 방향 바꿔서 이동.
    shark_info = []
    for i in range(R):
        for j in range(C):
            if table[i][j] > 0:
                shark_info.append((i, j, table[i][j]))
    # 상어 좌표, 번호
    for i in range(len(shark_info)):
        y, x, idx = shark_info[i]
        s_, d_, z_ = shark[idx][0], shark[idx][1], shark[idx][2]
        ny, nx = y, x
        if shark[idx][1] == 1 or shark[idx][1] == 2: # 위, 아래
            for j in range(s_):
                ny, nx = ny + xy[d_][0], nx
                if 0 > ny:
                    ny = 1
                    d_ = 2
                elif R <= ny:
                    ny = R - 2
                    d_ = 1
        elif shark[idx][1] == 3 or shark[idx][1] == 4: # 위, 아래
            for j in range(s_):
                ny, nx = ny, nx + xy[d_][1]
                if 0 > nx:
                    nx = 1
                    d_ = 3
                elif C <= nx:
                    nx = C - 2
                    d_ = 4
        if tmp[ny][nx] > 0: # 상어가 있다면 크기 비교
            pre_idx = tmp[ny][nx]
            pre_z = shark[pre_idx][2]
            if pre_z < z_: # 무게가 더 크면 잡아먹음
                tmp[ny][nx] = idx
        else:
            tmp[ny][nx] = idx
        shark[idx][1] = d_
    table = tmp




for i in range(C):
    # 낚시왕 이동
    p_idx = i
    # 열에 가장 가까운 상어를 잡는다.
    fishing()
    moveShark()
print(answer)