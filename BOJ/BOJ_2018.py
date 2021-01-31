N = int(input())

nums = [i for i in range(1, N+1)]
left, right, res = 0, 0, nums[0]
ans = 0
while left <= right:
    if res <= N:
        if res == N:
            ans += 1
        right += 1
        if right == len(nums):
            break
        res += nums[right]
    else:
        res -= nums[left]
        left += 1
print(ans)
