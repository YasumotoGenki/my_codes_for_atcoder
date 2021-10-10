k = int(input())
a, b = map(str, input().split())

decimal_a = 0
decimal_b = 0

for i in range(1, 20):
    if len(a) < i:
        pass
    else:
        decimal_a += int(a[-i]) * (k ** (i - 1))
    if len(b) < i:
        pass
    else:
        decimal_b += int(b[-i]) * (k ** (i - 1))

print(decimal_a * decimal_b)