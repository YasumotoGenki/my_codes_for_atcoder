n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

min_idx, max_idx = 0, 1
ans = 1
current_sum = 1

while(max_idx < n):
    if a[max_idx] - a[min_idx] < m:
        current_sum += 1
        ans = max(ans, current_sum)
        max_idx += 1
    else:
        min_idx += 1
        current_sum -= 1
print(ans)