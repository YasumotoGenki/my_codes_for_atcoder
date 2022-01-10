import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input())
s = input()

pre_char = ""
count = 0
ans = 0

for i in range(n):
    cur_char = s[i]
    if cur_char == pre_char:
        count += 1
    else:
        if count > 0:
            ans += combinations_count(count + 1, 2)
            count = 0
    pre_char = cur_char
else:
    if count > 0:
        ans += combinations_count(count + 1, 2)

print(ans)