n = int(input())
abcd =[]
for i in range(n):
    abcd.append(list(map(int, input().split())))

ans = 0
for x in range(1,101):
    for y in range(1, 101):
        for i in range(n):
            a, b, c, d = abcd[i]
            if a < x <= b and c < y <= d:
                ans += 1
                break

print(ans)