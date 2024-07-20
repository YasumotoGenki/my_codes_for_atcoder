a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

ans = True
# https://procon.fun/code/line-overlap/
if (a - j) * (d - g) < 0:
    pass
else:
    ans = False

if (b - k) * (e - h) < 0:
    pass
else:
    ans = False

if (c - l) * (f - i) < 0:
    pass
else:
    ans = False

if ans:
    print("Yes")
else:
    print("No")