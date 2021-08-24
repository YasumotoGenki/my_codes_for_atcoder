H, W = map(int, input().split())
A = []

for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

S_row = []
for i in range(H):
    S_row.append(sum(A[i]))

S_col = []
for i in range(W):
    col_sum = 0
    for j in range(H):
        col_sum += A[j][i]
    S_col.append(col_sum)

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(str(S_row[i] + S_col[j] - A[i][j]))
    print(" ".join(ans))