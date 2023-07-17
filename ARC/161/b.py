from itertools import combinations
from bisect import bisect_left

t = int(input())

# あり得るf(x)=3となる数を計算しておく
items = []
items += [i for i in range(60)]
possible_num_list = []

for comb in combinations(items, 3):
    current_num = 0
    for c in comb:
        current_num += (1 << c)
    possible_num_list.append(current_num)

possible_num_list.sort()
for i in range(t):
    n = int(input())
    idx = bisect_left(possible_num_list, n)
    if idx >= len(possible_num_list):
        print(-1)
    elif possible_num_list[idx] == n:
        print(n)
    elif idx > 0:
        print(possible_num_list[idx - 1])
    else:
        print(-1)