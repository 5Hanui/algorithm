N = int(input())
ans = ""

def backtrack(cnt, s):
    global ans
    for k in range(1, cnt // 2 + 1):
        a = int(s[cnt-k:])
        b = int(s[cnt - 2*k:cnt - k])
        if a == b: return

    if cnt == N:
        print(s)
        exit(0)
    for i in ["1", "2", "3"]:
        backtrack(cnt+1, s + i)


backtrack(1, '1')