a, b = map(int, input().split())
ans = 0
while(a !=  b):
    if a < b:
        a, b = b, a
    diff_ab = a - b
    if diff_ab % b == 0:
        count = a // b - 1
        ans += count
        a = b
    else:
        count = (diff_ab // b + 1)
        ans += count
        a -= (b * count)

print(ans)