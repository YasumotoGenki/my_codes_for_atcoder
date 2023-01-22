n, a, b = map(int, input().split())
s = input()

ans = b * (n // 2)

for i in range(n):
    cur_s = s[i:n] + s[:i]
    cost = i * a
    for j in range(n // 2):
        if cur_s[j] != cur_s[-1 - j]:
            cost += b
    ans = min(ans, cost)
print(ans)