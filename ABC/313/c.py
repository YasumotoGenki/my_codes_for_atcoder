n = int(input())
a = list(map(int, input().split()))

average = sum(a) / n

need_to_plus_count = 0
need_to_minus_count = 0

for i in range(n):
    if a[i] == average:
        pass
    elif a[i] < average:
        need_to_plus_count += int((average - a[i]) // 1)
    elif a[i] > average:
        need_to_minus_count += int((a[i] - average) // 1)
print(max(need_to_plus_count, need_to_minus_count))