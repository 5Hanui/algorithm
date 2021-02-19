import sys
input = sys.stdin.readline
N = int(input())
m = [0 for i in range(N)]
def check(c):
    # 윗줄까지만 체크하면 됨..
    # 겹치는 라인이 있는지 확인
    for j in range(c):
        if m[c] == m[j] or abs(m[c]-m[j]) == c - j:
            return False
    return True

ans = 0

def dfs(cnt):
    global ans
    if cnt == N:
        ans += 1
        return

    for i in range(N):
        m[cnt] = i
        if check(cnt):
            dfs(cnt+1)

dfs(0)
print(ans)
