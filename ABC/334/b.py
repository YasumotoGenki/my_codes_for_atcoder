a, m, l, r = map(int, input().split())

if l < a < r:
    ans = (r - a) // m + (a - l) // m + 1
elif l == a:
    ans = (r - l) // m + 1
elif r == a:
    ans = (r - l) // m + 1
elif a < l:
    ans = (r - a) // m - (l - 1 - a) // m
elif r < a:
    ans = (a - l) // m - (a - r - 1) // m
print(ans)
