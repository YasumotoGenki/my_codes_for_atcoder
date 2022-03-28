a = list(map(int, input().split()))

n = -1

for i in range(3):
    if n == -1:
        n = a[i]
    else:
        n = a[n]

print(n)