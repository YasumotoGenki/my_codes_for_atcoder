from scipy.special import comb


n = int(input())
a = list(map(int, input().split()))

ans = n

l_idx, r_idx = 0, 1

while(r_idx < n):
    if r_idx == n - 1:
        ans += comb(r_idx  - l_idx + 1, 2, exact=True)
        break
    if a[l_idx + 1] - a[l_idx] == a[r_idx + 1] - a[r_idx]:
        r_idx += 1
    else:
        ans += comb(r_idx  - l_idx + 1, 2, exact=True)
        l_idx = r_idx
        r_idx += 1

print(ans)