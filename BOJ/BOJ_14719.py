H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0
left = [0 for i in range(W)]
right = [0 for i in range(W)]
max_l, max_r = 0, 0

for i in range(W):
    max_l = max(block[i], max_l)
    left[i] = max_l


for i in range(W-1, -1, -1):
    max_r = max(block[i], max_r)
    right[i] = max_r


for i in range(W):
    max_len = min(left[i], right[i])
    if max_len > block[i]:
        ans += max_len - block[i]
print(ans)