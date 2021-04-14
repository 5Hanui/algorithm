import copy, heapq
N, M, D = map(int, input().split())
d = []
xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
num = 0
answer = 0
for i in range(N):
    arr = list(map(int, input().split()))
    d.append(arr)
    for j in range(M):
        if arr[j] == 1:
            num += 1

g = [0 for i in range(M)]
g_visit = [False for i in range(M)]
tmp = []

def findAndAttackEnemy(t):
    cnt = 0
    global tmp, D, num
    ee = []
    # 적이 있는 칸을 ee에 넣는다.
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 1:
                ee.append((i, j))

    attack = []
    for i in range(M):
        if t[i] == 1:
            attack_list = []
            for y, x in ee: #적의 위치
                dir_ = abs(y - N) + abs(x - i)
                # 공격할 수 위치에 있는 적을 찾아서 attack_list에 넣는다.
                if dir_ <= D:
                    heapq.heappush(attack_list, (dir_, x, y))
            if attack_list:
                person = heapq.heappop(attack_list)
                attack.append((person[2], person[1]))
    # 공격 실시, 공격받는 적 수 카운트
    for k in range(len(attack)):
        y, x = attack[k][0], attack[k][1]
        if tmp[y][x] == 1:
            tmp[y][x] = 0
            cnt += 1
    return cnt


def down():
    global tmp, num
    down_tmp = [[0 for i in range(M)] for _ in range(N)]
    count = 0
    for i in range(M):
        if tmp[N-1][i] == 1:
            count += 1
    # 한칸씩 내려보냄.
    for i in range(N-2, -1, -1):
        for j in range(M):
            if tmp[i][j] == 1:
                down_tmp[i][j] = 0
                down_tmp[i + 1][j] = 1
    tmp = copy.deepcopy(down_tmp)
    return count


def gameStart(g):
    global tmp, answer, num
    tmp_n = copy.deepcopy(num)
    count, d_count = 0, 0
    while tmp_n>0:
        # 공격할 가장 가까운 적을 찾는다
        count += findAndAttackEnemy(g)
        tmp_n = num - count
        # 적 한칸 아래로 이동
        d_count += down()
        tmp_n -= d_count
    answer = max(answer, count)



def arrange(cnt, idx): # 궁수 3명 배치
    global g, g_visit, tmp, d
    if cnt == 3: # 배치되면 게임 시작
        tmp = copy.deepcopy(d)
        gameStart(copy.deepcopy(g))
        return
    for i in range(idx, M):
        if g_visit[i] is False:
            g_visit[i] = True
            g[i] = 1
            arrange(cnt+1, i)
            g_visit[i] = False
            g[i] = 0


for i in range(M):
    if g_visit[i] is False:
        g_visit[i] = True
        g[i] = 1
        arrange(1, i)
        g_visit[i] = False
        g[i] = 0

print(answer)