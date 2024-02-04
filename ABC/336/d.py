n = int(input())
a = list(map(int, input().split()))
from_left_max_list = [0 for _ in range(n)]
from_right_max_list = [0 for _ in range(n)]

for i in range(n):
    from_left_max_list[i] = min(i + 1, a[i])
    if i > 0:
        from_left_max_list[i] = min(from_left_max_list[i - 1] + 1, from_left_max_list[i])

for i in range(n):
    from_right_max_list[-1-i] = min(i + 1, a[-1-i])
    if i > 0:
        from_right_max_list[-1-i] = min(from_right_max_list[-i] + 1, from_right_max_list[-1-i])

ans = 1
for i in range(n):
    ans = max(ans, min(from_left_max_list[i], from_right_max_list[i]))
print(ans)