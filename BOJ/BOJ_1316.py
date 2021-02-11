n = int(input())
arr = []
ans = 0
for i in range(n):
    string = input()
    arr.append(string)

def solution(str):
    d = dict()
    if len(str) == 1:
        return True
    d[str[0]] = 0
    for i in range(1, len(str)):
        if str[i-1] == str[i]:
            continue
        else:
            if str[i] in d:
                return False
            else:
                d[str[i]] = 0
    return True
for s in arr:
    if solution(s):
        ans += 1
print(ans)