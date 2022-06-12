from math import sqrt


a, b = map(int, input().split())

if a == 0:
    print(0, 1)
    exit()

k = (b / a)

x = sqrt(1 / (1 + k ** 2))
y = k * x
print(x, y)