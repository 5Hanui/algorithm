# i칸 만큼 회전
def moveString(string, i):
    return string[i:len(string)] + string[:i]


# 괄호 체크
def checkString(string):
    check_str = {'[': ']', '(': ')', '{': '}', ']': '[', ')': '(', '}': '{'}
    arr = list(string)
    stack = []
    for s in arr:
        if s == '(' or s == '[' or s == '{':
            stack.append(s)
        else:
            if len(stack) ==0 : return False
            cur = stack.pop()
            if cur != check_str[s]:
                return False
    if len(stack) > 0:
        return False
    return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        string = moveString(s, i)
        if checkString(string):
            answer += 1
    return answer

# print(solution("[](){}"))

print(solution("}]()[{"))