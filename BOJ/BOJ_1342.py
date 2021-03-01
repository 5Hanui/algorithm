string = input()
visit = [False for i in range(len(string))]
arr = list(string)
ret = set()
def backtrack(cnt, s):
    if cnt > 1 and s[-1] == s[-2]:
        return
    if len(arr) == len(s):
        ret.add(s)
        return
    for i in range(len(arr)):
        if visit[i] is False:
            visit[i] = True
            backtrack(cnt+1, s+arr[i])
            visit[i] = False

for i in range(len(arr)):
    if visit[i] is False:
        visit[i] = True
        backtrack(1, arr[i])
        visit[i] = False

print(len(ret))