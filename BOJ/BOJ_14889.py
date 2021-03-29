import sys
N = int(input())
d = []
answer = sys.maxsize
for i in range(N):
    arr = list(map(int, input().split()))
    d.append(arr)

visit = [False for i in range(N+1)]
def minus(arr1, arr2):
    s1, s2 = 0, 0
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            s1 += (d[arr1[i]-1][arr1[j]-1] + d[arr1[j]-1][arr1[i]-1])
            s2 += (d[arr2[i]-1][arr2[j]-1] + d[arr2[j]-1][arr2[i]-1])
    return abs(s1-s2)

def dfs(cnt, idx):
    global answer
    if cnt == N//2:
        tmp1 = []
        tmp2 = []
        for n in range(1, N+1):
            if visit[n] is True:
                tmp1.append(n)
            else:
                tmp2.append(n)
        answer = min(minus(tmp1, tmp2), answer)
        return

    for j in range(idx+1, N+1):
        visit[j] = True
        dfs(cnt + 1, j)
        visit[j] = False


for i in range(1, N+1):
    visit[i] = True
    dfs(1, i)
    visit[i] = False
print(answer)
