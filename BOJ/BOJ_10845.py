N = int(input())
q = []
ret = []
def solution(string):
    s = string.split()
    if s[0] == "push":
        q.append(int(s[1]))
    elif s[0] == "pop":
        if len(q) == 0:
            ret.append(-1)
        else:
            cur = q[0]
            del q[0]
            ret.append(cur)
    elif s[0] == "size":
        ret.append(len(q))
    elif s[0] == "empty":
        if len(q) == 0:
            ret.append(1)
        else:
            ret.append(0)
    elif s[0] == "front":
        if len(q) == 0:
            ret.append(-1)
        else:
            ret.append(q[0])
    elif s[0] == "back":
        if len(q) == 0:
            ret.append(-1)
        else:
            ret.append(q[-1])


for i in range(N):
    cmd = input()
    solution(cmd)

for i in ret:
    print(i)