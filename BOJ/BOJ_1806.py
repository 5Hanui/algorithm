N, S = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
right = 0
res = nums[0]
ans = 987654321
while left <= right and right < N:
    if res < S:
        right += 1
        if right == N:
            break
        res += nums[right]
    elif res == S:
        ans = min(ans, right - left + 1)
        right += 1
        if right == N:
            break
        res += nums[right]
    elif res > S:
        ans = min(ans, right - left + 1)
        res -= nums[left]
        left += 1


if ans == 987654321:
    print("0")
else:
    print(ans)