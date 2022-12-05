x, k = map(int, input().split())


for i in range(k):
    rem = x % (10 ** (i + 1))
    if rem < 5 * (10 ** i):
        x -= rem
    else:
        x += (10 ** (i + 1)) - rem

print(x)