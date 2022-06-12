n = int(input())

ans = []

for i in range(n):
    ans = ans + [i + 1] + ans
print(*ans)