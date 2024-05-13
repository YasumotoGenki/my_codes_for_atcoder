n = int(input())

diff_max = -1
diff_max_idx = 0
ab = []

for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
    diff = b - a
    if diff_max < diff:
        diff_max = diff
        diff_max_idx = i

ans = 0
for i in range(n):
    if  diff_max_idx != i:
        ans += ab[i][0]
    else:
        ans += ab[i][1]

print(ans)