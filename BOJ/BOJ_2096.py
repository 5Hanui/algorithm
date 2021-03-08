N = int(input())
d = [list(map(int, input().split())) for i in range(N)]

large = d[0]
small = d[0]

for i in range(1, N):
    large = [max(large[0], large[1]) + d[i][0],
             max(large[0], large[1], large[2]) + d[i][1],
             max(large[1], large[2]) + d[i][2]]
    small = [min(small[0], small[1]) + d[i][0],
             min(small[0], small[1], small[2]) + d[i][1],
             min(small[1], small[2]) + d[i][2]]


print(max(large), min(small))
