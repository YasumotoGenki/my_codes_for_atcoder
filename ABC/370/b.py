n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    cur_list = list(map(int, input().split()))
    for j in range(len(cur_list)):
        a[i][j] = cur_list[j]
        a[j][i] = cur_list[j]

idx = 1
for i in range(n):
    idx = a[idx - 1][i]

print(idx)