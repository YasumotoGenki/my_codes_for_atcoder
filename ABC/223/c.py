n = int(input())
list_a, list_b = [], []
list_time = []

for i in range(n):
    a, b = map(int, input().split())
    t = a / b
    list_a.append(a)
    list_b.append(b)
    list_time.append(t)

sum_time = sum(list_time)

pre_time = 0

for i in range(n):
    if pre_time + list_time[i] > sum_time / 2:
        idx = i
        break
    else:
        pre_time += list_time[i]

rem_time = sum_time / 2 - pre_time

ans = sum(list_a[:idx]) + rem_time * list_b[idx]
print(ans)