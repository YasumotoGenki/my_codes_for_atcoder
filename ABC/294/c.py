n, m = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_c = list_a + list_b
list_c.sort()

idx_a = 0
idx_b = 0
ans_list_a_indices_list = []
ans_list_b_indices_list = []
for i in range(n + m):
    if idx_a < n and list_a[idx_a] == list_c[i]:
        ans_list_a_indices_list.append(i + 1)
        idx_a += 1
    else:
        ans_list_b_indices_list.append(i + 1)
        idx_b += 1
print(*ans_list_a_indices_list)
print(*ans_list_b_indices_list)