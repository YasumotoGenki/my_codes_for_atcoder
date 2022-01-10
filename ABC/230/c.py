n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

coordinate = [['.' for i in range(s - r + 1)] for j in range(q - p + 1)]

for k in range(max(max(1 - a, 1 - b), p - a), min(min(n - a, n - b) + 1, q - a + 1)):
    if p <= a + k <= q and r <= b + k <= s:
        coordinate[a + k - p][b + k - r] = '#'

for k in range(max(max(1 - a, b - n), p - a) , min(min(n - a, b - 1) + 1, q - a + 1)):
    if p <= a + k <= q and r <= b - k <= s:
        coordinate[a + k - p][b - k - r] = '#'

for i in range(len(coordinate)):
    print(''.join(map(str, coordinate[i])))
        