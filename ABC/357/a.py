n, m = map(int, input().split())
h = list(map(int, input().split()))

for i in range(n):
    if m < h[i]:
        print(i)
        exit()
    else:
        m -= h[i]

print(n)