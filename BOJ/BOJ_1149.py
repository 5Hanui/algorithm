N = int(input())
d = []
mem = [[0 for i in range(3)] for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    d.append(arr)

def dp(r):
    if r == N:
        return
    for i in range(3):
        if i == 0:
            mem[r][i] = min(mem[r-1][1] + d[r][i], mem[r-1][2] + d[r][i])
        elif i == 1:
            mem[r][i] = min(mem[r - 1][0] + d[r][i], mem[r - 1][2] + d[r][i])
        elif i == 2:
            mem[r][i] = min(mem[r - 1][0] + d[r][i], mem[r - 1][1] + d[r][i])
    dp(r + 1)


for i in range(3):
    mem[0][i] = d[0][i]
    dp(1)
print(min(mem[N-1]))