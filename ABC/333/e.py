n = int(input())

tx = []
t2x_set = set()

for _ in range(n):
    tx.append(list(map(int, input().split())))
    if tx[-1][0] == 2:
        t2x_set.add(tx[-1][1] - 1)

count_list = [0 for _ in range(n)]

for t, x in tx:
    if t == 1:
        count_list[x - 1] += 1
    else:
        count_list[x - 1] -= 1
        if count_list[x - 1] < 0:
            print(-1)
            exit()

count_list = [0 for _ in range(n)]
count = 0
ans = 0
act_list = []
for t, x in reversed(tx):
    if t == 1:
        if count_list[x - 1] > 0:
            count_list[x - 1] -= 1
            count -= 1
            act_list.append(1)
        else:
            act_list.append(0)
    else:
        if x - 1 in t2x_set:
            count_list[x - 1] += 1
            count += 1
            ans = max(ans, count)
print(ans)
print(*reversed(act_list))