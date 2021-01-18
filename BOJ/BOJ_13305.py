N = int(input())
dist = list(map(int, input().split()))
city = list(map(int, input().split()))
answer = 0
result = city
for i in range(1, len(result)):
    if city[i-1] > city[i]:
        result[i] = city[i]
    else:
        result[i] = city[i-1]

for i in range(len(dist)):
    answer += dist[i] * result[i]
print(answer)