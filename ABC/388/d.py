n = int(input())
a = list(map(int, input().split()))

b = [a[i] for i in range(n)]
give_stone_num = 0
lost_stone_timing = [0 for _ in range(n)]
for i in range(n):
    b[i] += give_stone_num
    if b[i] > 0 and i < n - 1:
        give_stone_num += 1
        if b[i] < n - i - 1:
            lost_stone_timing[i + b[i]] += 1
            b[i] = 0
        else:
            b[i] -= n - i - 1
    give_stone_num -= lost_stone_timing[i]

print(*b)
