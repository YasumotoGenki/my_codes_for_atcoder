n = int(input())
l, r = None, None
ans = 0
for _ in range(n):
    a, s = map(str, input().split())
    a = int(a)
    if s == "L":
        if l is not None:
            ans += abs(l - a)
        l = a
    else:
        if r is not None:
            ans += abs(r - a)
        r = a

print(ans)