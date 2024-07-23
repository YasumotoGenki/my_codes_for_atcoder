n, t, p = map(int, input().split())
l = list(map(int, input().split()))

for i in range(100):
    count = 0
    for j in range(n):
        if l[j] + i >= t:
            count += 1
    if count >= p:
        print(i)
        exit()