from itertools import permutations, combinations

k = int(input())

num_list = [str(i) for i in range(10)]
candidates = []

for i in range(1, 11):
    for comb in combinations(num_list, i):
        comb = list(comb)
        comb.sort(reverse=True)
        cur_num_str = "".join(comb)
        cur_num_int = int(cur_num_str)
        candidates.append(cur_num_int)
candidates.sort()
# 0が不要のため
print(candidates[k])