N, M = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, max(arr)
answer = 0
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            s += arr[i] - mid
    if s >= M:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)