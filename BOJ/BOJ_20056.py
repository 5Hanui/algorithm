from collections import deque
N, M, K = map(int, input().split())
info = [[[] for i in range(N)] for j in range(N)]  # 0: 질량, 1: 속력, 2: 갯수
q = deque()
# 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
dir_ = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for i in range(M):
    arr = list(map(int, input().split()))
    info[arr[0]-1][arr[1]-1].append((arr[0]-1, arr[1]-1, arr[2], arr[3], arr[4]))

answer = 0
def move():
    # m: 질량, d: 방향, s: 속력
    # ri, ci, mi, si, di
    global q, dir_, info, answer, N
    tmp_info = [[[] for i in range(N+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(N):
            while info[i][j]:
                cur = info[i][j].pop()
                y, x, m, s, d = cur[0], cur[1], cur[2], cur[3], cur[4]
                ny, nx = (y + (dir_[d][0] * s) ) % N, (x + (dir_[d][1] * s) ) % N
                tmp_info[ny][nx].append((ny, nx, m, s, d))
    info = tmp_info


def addAndDevide():
    global info, q, answer
    tmp = [[[] for i in range(N + 1)] for j in range(N + 1)]

    for i in range(N):
        for j in range(N):
            if len(info[i][j]) >= 2:
                m, s, d1, d2 = 0, 0, 0, 0 # 질량합, 속력합, 짝수인 합, 홀수인 합
                cnt = len(info[i][j])
                while info[i][j]:
                    cur = info[i][j].pop()
                    m += cur[2]
                    s += cur[3]
                    if cur[4] % 2 == 0:
                        d1 += 1
                    else:
                        d2 += 1
                mg, ss = m // 5, s // cnt
                if mg == 0:
                    continue
                if d1 == 0 or d2 == 0: #모두 홀수 거나 모두 짝수이면,
                    # 0,2,4,6
                    for nd in [0, 2, 4, 6]:
                        tmp[i][j].append([i, j, mg, ss, nd])
                else:
                    for nd in [1, 3, 5, 7]:
                        tmp[i][j].append([i, j, mg, ss, nd])
            else:
                tmp[i][j] = info[i][j]
    info = tmp

while K > 0:
    K -= 1
    # 모든 파이어볼 이동
    move()
    # 합친다
    addAndDevide()
for i in range(N):
    for j in range(N):
        for k in range(len(info[i][j])):
            answer += info[i][j][k][2]
print(answer)