N = int(input())
left, right = 0, 0
res = 0
primes = []
nums = [True for _ in range(N+1)]
m = int(N ** 0.5)
if N == 1:
    print("0")
    exit(0)
for i in range(2, m+1):
    if nums[i]:
        for j in range(i+i, N+1, i):
            nums[j] = False
primes = [i for i in range(2, N+1) if nums[i] is True]
res = primes[0]
ans = 0
while left <= right and right < len(primes):
    if res <= N:
        if res == N:
            ans += 1
        right += 1
        if right == len(primes):
            break
        res += primes[right]
    elif res > N:
        res -= primes[left]
        left += 1

print(ans)