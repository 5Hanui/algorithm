S = list(input())
T = list(input())
answer = 0
while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
    if S == T:
        answer = 1
        break


print(answer)