N, K = map(int, input().split())
d = list(map(int, input().split()))
start, end = 0, 0
s = d[start]
ans = 1000000 * -100
while start <= end:
    if end - start == K - 1:
        ans = max(ans, s)
    if end < start + K:
        end += 1
        if end == N:
            break
        s += d[end]

    else:
        s -= d[start]
        start += 1
print(ans)