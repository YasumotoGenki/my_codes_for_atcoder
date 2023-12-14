n, m = map(int, input().split())
s = input()

count_2 = 0
count_1 = 0
ans = 0
for item in s:
    if item == "0":
        ans = max(ans, count_2 + max(count_1 - m, 0))
        count_2 = 0
        count_1 = 0
    elif item == "1":
        count_1 += 1
    else:
        count_2 += 1
ans = max(ans, count_2 + max(count_1 - m, 0))
print(ans)