N = int(input())
d = list(map(int, input().split()))
M = int(input())
d.sort()
left, right = 0, max(d)
ans = 0
ret = 0
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in range(len(d)):
        if mid < d[i]:
            s += mid
        else:
            s += d[i]
    if s <= M:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)