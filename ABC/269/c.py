from itertools import combinations

n = int(input())

bin_indices = []
for i in range(60):
    cur = 1 << i
    if cur & n:
        bin_indices.append(i)

candidates = [0]
for i in range(1, len(bin_indices) + 1):
    for items in combinations(bin_indices, i):
        cur = 0
        for item in items:
            cur += 1 << item
        candidates.append(cur)

candidates.sort()
for item in candidates:
    print(item)