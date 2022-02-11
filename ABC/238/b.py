n = int(input())
a = list(map(int, input().split()))

cut_list = [0]
pre = 0
for i in range(n):
    cur = a[i] + pre
    if cur > 360:
        cur -= 360
    cut_list.append(cur)
    pre = cur

cut_list.sort()

ans = 0
for i in range(n - 1):
    ans = max(ans, cut_list[i + 1] - cut_list[i])
last_piece = cut_list[0] - cut_list[-1]
if last_piece < 0:
    last_piece += 360
ans = max(ans, last_piece)
print(ans)