N = int(input())
cmd_list = []
arr = []
ret = []
def solution(string):
    s = string.split()
    if s[0] == "push":
        arr.append(int(s[1]))
    elif s[0] == "pop":
        if len(arr) == 0:
            ret.append(-1)
        else:
            ret.append(arr.pop())
    elif s[0] == "size":
        ret.append(len(arr))
    elif s[0] == "empty":
        if len(arr) == 0:
            ret.append(1)
        else:
            ret.append(0)
    elif s[0] == "top":
        if len(arr) == 0:
            ret.append(-1)
        else:
            ret.append(arr[-1])

for i in range(N):
    cmd = input()
    solution(cmd)

for i in ret:
    print(i)