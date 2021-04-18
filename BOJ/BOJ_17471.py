from collections import deque
N = int(input())
m = [[] for i in range(N+1)]
arr = list(map(int, input().split()))
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    m[i] += tmp[1:]
visit = [False for i in range(N+1)]
teamA = []
answer = 987654321

def bfs(a):
    global arr
    q = deque()
    visitA = [False for i in range(N+1)]
    q.append(a[0])
    visitA[a[0]] = 1
    cnt = 1
    while q:
        cur = q.popleft()
        for n in m[cur]:
            if n in a and visitA[n] is False:
                q.append(n)
                cnt += 1
                visitA[n] = True
    if cnt < len(a): # 다연결이 안되어있으면 0
        return 0
    s = 0
    for num in a: #다연결 되어있으면 인구수
        s += arr[num-1]
    return s


def check(a):
    # bfs로 팀끼리 연결이 되어있는지 체크
    global answer
    b = [i for i in range(1, N+1)]
    for i in a:
        b.remove(i)
    if len(a) == 0 or len(b) == 0: # 구역에 하나라도 포함되어야한다.
        return
    numA = bfs(a)
    numB = bfs(b)

    if numA != 0 and numB != 0: # 모두다 연결되어있다면 최소 인구수 계산
        answer = min(answer, abs(numA - numB))


def devideTeam(idx):
    global answer, teamA, visit
    check(teamA)
    for i in range(idx+1, N + 1):
        if visit[i] is False:
            visit[i] = True
            teamA.append(i)
            devideTeam(i)
            visit[i] = False
            teamA.pop()


for j in range(1, N+1):
    if visit[j] is False:
        visit[j] = True
        teamA.append(j)
        devideTeam(j)
        visit[j] = False
        teamA.pop()
if answer == 987654321:
    print(-1)
else:
    print(answer)
