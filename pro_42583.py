from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    q = deque(truck_weights)
    cnt = 0 # 지나간 트럭수
    temp = 0
    while True:
        answer += 1
        if len(q) == 0 and cnt == len(truck_weights):
            break
        if len(q) > 0 and len(bridge) < bridge_length and temp + q[0] <= weight: # 이동 가능
            cur = q.popleft()
            temp += cur
            bridge.append((cur, answer)) # ( 무게, 들어간 시점)

        if len(bridge) > 0:
            w, time = bridge[0]
            if answer - time + 1 == bridge_length:
                ww, t = bridge.popleft()
                temp -= ww
                cnt += 1
    return answer
