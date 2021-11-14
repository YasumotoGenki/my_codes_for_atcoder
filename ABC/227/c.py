import math
n = int(input())

ans = 0
for a in range(1, 10 ** 4):
    if a ** 3 > n:
        break
    upper_lim_b = int(math.sqrt(n / a)) + 2
    for b in range(a, upper_lim_b):
        if int(n / a / b) < b:
            continue
        ans += int(n / a / b) - b + 1

print(ans)
