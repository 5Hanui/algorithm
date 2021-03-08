num = int(input())
d = [0 for i in range(num+1)]
d[0] = 0
d[1] = 1

def fivonachi(n):
    if n == 0 or n == 1:
        return d[n]
    if d[n] > 0:
        return d[n]
    d[n] = fivonachi(n-2) + fivonachi(n-1)
    return d[n]
fivonachi(num)
print(d[num])