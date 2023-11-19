n = int(input())
d = list(map(int, input().split()))

ans = 0
for month in range(1, n + 1):
    str_month = str(month)
    for day in range(1, d[month - 1] + 1):
        str_day = str(day)
        if len(set(str_month) | set(str(day)))  == 1:
            ans += 1

print(ans)