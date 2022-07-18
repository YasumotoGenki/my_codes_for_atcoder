n, x, y = map(int, input().split())

red = [0 for _ in range(n)]
blue = [0 for _ in range(n)]
red[n - 1] = 1

for i in range(n - 1, 0, -1):
    red[i - 1] += red[i]
    blue[i] += red[i] * x
    red[i - 1] += blue[i]
    blue[i - 1] += blue[i] * y
print(blue[0])
