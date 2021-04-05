N, K = map(int, input().split())
d = list(map(int, input().split()))

belt = []
step = 0
for i in range(len(d)):
    belt.append([d[i], False])

# 한칸 회전
def spiral():
    global belt
    # N번째 있으면 내려감.
    if belt[N-1][1] is True:
        belt[N-1][1] = False
    new_belt = list()
    new_belt.append(belt[len(belt)-1])
    new_belt += belt[:len(belt)-1]
    belt = new_belt


def moveRobot():
    global belt
    for i in range(N-1, -1, -1):
        if belt[i][1] is True:
            if i == N-1: #내려감.
                belt[i][1] = False
            else: # 한칸씩 이동
                if belt[i+1][1] is False and belt[i+1][0] > 0:
                    belt[i+1][0] -= 1
                    belt[i][1] = False
                    belt[i + 1][1] = True


def addRobot():
    global belt
    a, robotYn = belt[0][0], belt[0][1]
    if robotYn is False and belt[0][0] > 0:
        belt[0][0] -= 1
        belt[0][1] = True


while True:
    step += 1
    spiral()
    moveRobot()
    addRobot()
    s = 0
    for i in range(len(belt)):
        if belt[i][0] == 0:
            s += 1
    if s >= K:
        break

print(step)