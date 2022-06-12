h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

points = []
for hi in range(h):
    for wi in range(w):
        if s[hi][wi] == "o":
            points.append([hi, wi])
h1, w1 = points[0]
h2, w2 = points[1]

ans = abs(h1 - h2) + abs(w1 - w2)
print(ans)