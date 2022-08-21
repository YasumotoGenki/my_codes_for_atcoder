x, y, n = map(int, input().split())

if x * 3 <= y:
    ans = x * n
else:
    ans = (n // 3) * y + (n % 3) * x
print(ans)