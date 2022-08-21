from itertools import combinations

n, m = map(int, input().split())

for item in combinations([i for i in range(1, m + 1)], n):
    print(*item)