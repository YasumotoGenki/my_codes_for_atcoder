r = int(input())

y = r * 10 + 5
ans = 0
for i in range(0, r * 10, 10):
    x = i + 5
    while(y > 10 and x ** 2 + y ** 2 > (r * 10) ** 2):
        y -= 10
    if i == 0:
        ans += (y + 5) // 10 * 2 - 1
    else:
        ans += ((y + 5) // 10 * 2 - 1) * 2

print(ans)