n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("Yes")
    exit()

a.sort()

large_num_min_idx = (n // 2) + 1
large_num = a[large_num_min_idx]
large_num_min_count = a[large_num_min_idx:].count(large_num)

idx = 0
smaller_num_count = 0
while(idx < large_num_min_idx):
    if a[idx] < large_num:
        smaller_num_count += 1
    if smaller_num_count > large_num_min_count:
        print("Yes")
        exit()
    idx += 1
print("No")