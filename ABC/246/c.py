n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

for i in range(len(a)):
    if a[i] > x:
        if a[i] // x <= k:
            used_num = a[i] // x
            k -= used_num
            a[i] -= used_num * x
        else: #if a[i] // x > k:
            a[i] = a[i] - k * x
            k = 0
            print(sum(a))
            exit()

a.sort(reverse=True)
for i in range(min(k, n)):
    a[i] = 0
print(sum(a))
