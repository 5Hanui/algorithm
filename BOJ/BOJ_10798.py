strArr = list()
maxLen = 0
for i in range(5):
    arr = list(input())
    if len(arr) >= maxLen:
        maxLen = len(arr)
    strArr.append(arr)
printStr = ''
for i in range(maxLen):
    for j in range(5):
        if len(strArr[j]) <= i:
            continue
        if strArr[j][i]:
            printStr += strArr[j][i]
print(printStr)