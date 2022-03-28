n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = []

for i in range(n + 1):
    if a[i] == 0:
        pass
    else:
        min_a_idx = i
        min_a = a[i]
        break


for i in range(m + 1):
    cur_c = c[i + min_a_idx]
    sum_polynomial = 0
    # idx for b[j]
    for j in range(i):
        if min_a_idx + i - j <= n:
            sum_polynomial += a[min_a_idx + i - j] * b[j]
    cur_b = (cur_c - sum_polynomial) // min_a
    b.append(cur_b)

print(*b)