n = int(input())
arr = list(map(int, input().split()))
rank = [0 for i in range(n)]
st = []
for i in range(n):
    if len(st) == 0:
        rank[i] = 0
    else:
        while st:
            pre_idx, pre_num = st[-1][0], st[-1][1]
            if pre_num > arr[i]:
                rank[i] = pre_idx
                break
            st.pop()
    st.append((i+1, arr[i]))

for i in range(n):
    print(rank[i], end=' ')

