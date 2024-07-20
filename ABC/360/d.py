from bisect import bisect_left

n, t = map(int, input().split())
s = input()
x = list(map(int, input().split()))

right_directions = []
left_directions = []

for i in range(n):
    if s[i] == '1':
        right_directions.append(x[i])
    else:
        left_directions.append(x[i])

right_directions.sort()
left_directions.sort()

ans = 0
for i in range(len(right_directions)):
    p = right_directions[i]
    idx = bisect_left(left_directions, p)
    cross_idx = bisect_left(left_directions, p + 2 * t + 1)
    ans += cross_idx - idx

print(ans)