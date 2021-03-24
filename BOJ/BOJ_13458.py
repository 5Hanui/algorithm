N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

ans1, ans2 = 0, 0
for i in range(len(arr)):
    ans1 += 1
    b = arr[i] - B
    if b > 0:
        tmp_a, tmp_b = divmod(b, C)
        ans2 += tmp_a
        if tmp_b > 0:
            ans2 += 1

print(ans1 + ans2)