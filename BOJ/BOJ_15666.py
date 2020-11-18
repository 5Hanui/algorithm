N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
answer = []


def backtracking(idx, cnt):
    if cnt == M:
        for i in answer:
            print(i, end=' ')
        print()
        return
    for i in range(idx, len(nums)):
        answer.append(nums[i])
        backtracking(i, cnt+1)
        answer.pop()


def solution():
    for i in range(len(nums)):
        answer.append(nums[i])
        backtracking(i, 1)
        answer.pop()


solution()