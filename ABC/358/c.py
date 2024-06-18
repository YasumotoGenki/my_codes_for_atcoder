n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())

ans = n
for i in range(1 << n):
    flgs = [False for _ in range(m)]
    count = 0
    for j in range(n):
        if i & 1 << j:
            count += 1
            for k in range(m):
                if s[j][k] == "o":
                    flgs[k] = True
    if all(flgs):
        ans = min(ans, count)

print(ans)