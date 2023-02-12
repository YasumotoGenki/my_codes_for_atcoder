n, m = map(int, input().split())
a = list(map(int, input().split()))

if m == 0:
    ans = [i for i in range(1, n + 1)]
    print(*ans)
    exit()

min_n_idx = 1
max_n_idx = 1
a_idx = 0
ans = []
while(len(ans) < n):
    if a[a_idx] == max_n_idx:
        max_n_idx += 1
        if a_idx < m - 1:
            a_idx += 1
    else:
        for i in range(max_n_idx, min_n_idx - 1, -1):
            ans.append(i)
        max_n_idx += 1
        min_n_idx = max_n_idx
print(*ans)