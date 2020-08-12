N, M = map(int, input().split())
visit = [False for i in range(0, 10)]
cache = list();


def dfs(cnt, idx):
    if cnt == M:
        for num in range(1, len(visit)):
            if visit[num]:
                print(num, end=' ')
        print()

    for i in range(idx+1, N + 1):
        if not visit[i]:
            visit[i] = True
            dfs(cnt + 1, i)
            visit[i] = False


for i in range(1, N + 1):
    visit[i] = True
    dfs(1, i)
    visit[i] = False
