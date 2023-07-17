n = int(input())
a = list(map(int, input().split()))

num_counter = dict()
f = dict()

for i in range(3 * n):
    # count
    if a[i] not in num_counter:
        num_counter[a[i]] = 1
    else:
        num_counter[a[i]] += 1
    if num_counter[a[i]] == 2:
        f[a[i]] = i

paired_list = []
for i in range(1, n + 1):
    paired_list.append([i, f[i]])

paired_list.sort(key=lambda x:x[1])
ans = []
for i in range(n):
    ans.append(str(paired_list[i][0]))
print(" ".join(ans))