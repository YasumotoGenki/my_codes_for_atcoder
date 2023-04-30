from bisect import bisect_left
from math import floor

n = int(input())

prime_num_tf = [True for _ in range(10 ** 6 + 1)]
prime_num_tf[0] = False
prime_num_tf[1] = False

for i in range(2, 10 ** 6 + 1):
    if prime_num_tf[i] == False:
        continue
    for j in range(i * 2, 1000001, i):
        prime_num_tf[j] = False
prime_num = []
for i in range(len(prime_num_tf)):
    if i >= n ** 0.5:
        break
    if prime_num_tf[i] and i < n:
        prime_num.append(i)
ans = 0
for idx_a, a in enumerate(prime_num):
    for idx_b in range(idx_a + 1, len(prime_num)):
        b = prime_num[idx_b]
        limit = n // (a ** 2) // b
        limit = floor(limit ** 0.5)
        if limit < b:
            break
        c_max_idx = bisect_left(prime_num, limit)
        if c_max_idx == len(prime_num):
            c_max_idx -= 1
        if prime_num[c_max_idx] > limit:
            c_max_idx -= 1
        idx_c = idx_b + 1
        if c_max_idx < idx_c:
            break
        # print(limit)
        # print(a, b, c_max_idx, idx_c)
        ans += (c_max_idx - idx_c + 1)
print(ans)