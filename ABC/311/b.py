n, d = map(int, input().split())
s= []
for i in range(n):
    s.append(input())

count = 0
ans = 0
for day in range(d):
    all_ok_flg = True
    for i in range(n):
        if s[i][day] == "x":
            all_ok_flg = False
    if all_ok_flg:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
ans = max(ans, count)
print(ans)