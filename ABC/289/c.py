from itertools import combinations

n, m = map(int, input().split())
s = []
for i in range(m):
    c = input()
    s.append(set(list(map(int, input().split()))))

ans = 0
indices = [i for i in range(m)]
all_num_list = [i for i in range(1, n + 1)]
all_set = set(all_num_list)

for i in range(1, m + 1):
    for items in combinations(s, i):
        items_set = set()
        for j in range(i):
            items_set |= set(items[j])
        if all_set == items_set:
            ans += 1
print(ans)